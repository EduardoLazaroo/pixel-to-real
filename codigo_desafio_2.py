import argparse
import glob
import os
import re

import cv2
import numpy as np
import matplotlib.pyplot as plt


def natural_sort_key(path):
    base = os.path.basename(path)
    parts = re.split(r"(\d+)", base)
    return [int(p) if p.isdigit() else p.lower() for p in parts]


def crop_center(img, dim=256):
    h, w = img.shape[:2]
    starty = max(0, h // 2 - dim // 2)
    startx = max(0, w // 2 - dim // 2)
    return img[starty:starty + dim, startx:startx + dim]


def align_images(f, g, dim=256):
    # EXPERIMENTO 1 - Alinhamento e normalização das imagens
    if f.shape != (dim, dim):
        if f.shape[0] >= dim and f.shape[1] >= dim:
            f = crop_center(f, dim)
        else:
            f = cv2.resize(f, (dim, dim), interpolation=cv2.INTER_AREA)

    if g.shape != (dim, dim):
        if g.shape[0] >= dim and g.shape[1] >= dim:
            g = crop_center(g, dim)
        else:
            g = cv2.resize(g, (dim, dim), interpolation=cv2.INTER_LINEAR)

    return f.astype(np.float32), g.astype(np.float32)


def load_gray_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Não foi possível carregar a imagem: {path}")
    return img


def list_images(folder, extensions):
    paths = []
    for ext in extensions:
        paths.extend(glob.glob(os.path.join(folder, ext)))
    return sorted(paths, key=natural_sort_key)


def extract_first_integer(path):
    match = re.search(r"(\d+)", os.path.basename(path))
    return int(match.group(1)) if match else None


def pair_paths(synth_paths, capture_paths):
    synth_by_num = {extract_first_integer(p): p for p in synth_paths if extract_first_integer(p) is not None}
    capture_by_num = {extract_first_integer(p): p for p in capture_paths if extract_first_integer(p) is not None}

    if len(synth_by_num) == len(synth_paths) and len(capture_by_num) == len(capture_paths):
        common = sorted(set(synth_by_num) & set(capture_by_num))
        if common:
            return [(synth_by_num[n], capture_by_num[n]) for n in common]

    pairs = []
    count = min(len(synth_paths), len(capture_paths))
    for i in range(count):
        pairs.append((synth_paths[i], capture_paths[i]))
    return pairs


def plot_difference(f, g, title_prefix):
    # EXPERIMENTO 1 - Diferença entre modelo ideal e aquisição real
    print("EXPERIMENTO 1 - Diferença entre imagem sintética e capturada")

    diff = g - f

    plt.figure(figsize=(10, 4))
    plt.subplot(131)
    plt.imshow(f, cmap='gray')
    plt.title('Imagem Sintética')
    plt.axis('off')

    plt.subplot(132)
    plt.imshow(g, cmap='gray')
    plt.title('Imagem Capturada')
    plt.axis('off')

    plt.subplot(133)
    plt.imshow(np.abs(diff), cmap='jet')
    plt.title('Diferença |g - f|')
    plt.colorbar(fraction=0.046, pad=0.04)
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    return diff


def plot_edge_profile(f, g, row, col_slice, title_prefix):
    # EXPERIMENTO 2 - Suavização de bordas
    print("EXPERIMENTO 2 - Análise da suavização de bordas")

    perfil_f = f[row, col_slice]
    perfil_g = g[row, col_slice]

    plt.figure(figsize=(6, 4))
    plt.plot(perfil_f, label='Sintética (degrau)')
    plt.plot(perfil_g, label='Capturada (suavizada)')
    plt.title('Perfil de intensidade da borda')
    plt.legend()
    plt.grid()
    plt.show()

    return perfil_f, perfil_g


def plot_noise_histogram(n, title_prefix):
    # EXPERIMENTO 3 - Modelagem de ruído
    print("EXPERIMENTO 3 - Histograma do ruído estimado")

    plt.figure(figsize=(6, 4))
    plt.hist(n.ravel(), bins=50, density=True)
    plt.title('Histograma do ruído')
    plt.grid()
    plt.show()


def simulate_noise(f, g, n):
    # EXPERIMENTO 4 - Simulação de degradação
    print("EXPERIMENTO 4 - Simulação de degradação com ruído")

    media_ruido = np.mean(n)
    desvio_ruido = np.std(n)

    print(f"Média do ruído: {media_ruido:.4f}")
    print(f"Desvio padrão do ruído: {desvio_ruido:.4f}")

    n_s = np.random.normal(media_ruido, desvio_ruido, f.shape)
    g_s = np.clip(f + n_s, 0, 255)

    mse = np.mean((g - g_s) ** 2)
    psnr = 10 * np.log10((255 ** 2) / mse) if mse > 0 else float('inf')

    print(f"MSE: {mse:.2f}")
    print(f"PSNR: {psnr:.2f} dB\n")

    return mse, psnr, g_s


def plot_blur_metrics(esf, title_prefix):
    # EXPERIMENTO 5 - Estimativa do desfoque
    print("EXPERIMENTO 5 - Estimativa do desfoque (ESF/LSF)")

    lsf = np.gradient(esf)

    v_min, v_max = np.min(esf), np.max(esf)
    p10 = v_min + 0.10 * (v_max - v_min)
    p90 = v_min + 0.90 * (v_max - v_min)

    x10 = np.argmax(esf >= p10)
    x90 = np.argmax(esf >= p90)

    delta_x = abs(x90 - x10)

    print(f"Posição 10%: {x10}")
    print(f"Posição 90%: {x90}")
    print(f"Largura da transição (Delta X): {delta_x} pixels\n")

    fig, ax1 = plt.subplots(figsize=(6, 4))
    ax1.plot(esf, label='ESF')
    ax1.axvline(x10, linestyle='--', label='10%')
    ax1.axvline(x90, linestyle='--', label='90%')

    ax2 = ax1.twinx()
    ax2.plot(lsf, alpha=0.5, label='LSF')

    plt.title('Análise de desfoque')
    fig.legend()
    plt.grid()
    plt.show()


def compare_pair(synth_path, capture_path, dim=256):
    print("\n========================================")
    print(f"Comparando: {synth_path} com {capture_path}")
    print("========================================\n")

    f = load_gray_image(synth_path)
    g = load_gray_image(capture_path)

    f, g = align_images(f, g, dim=dim)

    # EXPERIMENTO 1
    plot_difference(f, g, "Comparação")

    # EXPERIMENTO 2
    row = min(128, f.shape[0] - 1)
    col_start = min(100, f.shape[1] - 2)
    col_end = min(150, f.shape[1])

    perfil_f, perfil_g = plot_edge_profile(
        f, g, row, slice(col_start, col_end), "Borda"
    )

    # EXPERIMENTO 3
    n = g[20:100, 20:100] - f[20:100, 20:100]
    plot_noise_histogram(n, "Ruído")

    # EXPERIMENTO 4
    simulate_noise(f, g, n)

    # EXPERIMENTO 5
    plot_blur_metrics(perfil_g, "Desfoque")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--synthetic')
    parser.add_argument('--capture')
    parser.add_argument('--capture-dir', default='imgs')
    parser.add_argument('--dim', type=int, default=256)
    parser.add_argument('--all', action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if args.synthetic and args.capture:
        compare_pair(args.synthetic, args.capture, dim=args.dim)
        return

    synthetic_paths = list_images(base_dir, ['*.ppm'])
    capture_dir = os.path.join(base_dir, args.capture_dir)
    capture_paths = list_images(capture_dir, ['*.jpg', '*.png'])

    pairs = pair_paths(synthetic_paths, capture_paths)

    for synth_path, capture_path in pairs:
        compare_pair(synth_path, capture_path, dim=args.dim)


if __name__ == '__main__':
    main()