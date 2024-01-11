from pathlib import Path

import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim


class ImgsConcdAnalyzer:

    def __init__(self, img1_path: str, img2_path: str) -> None:
        if not Path(img1_path).exists():
            raise FileNotFoundError(f'{img1_path}')
        if not Path(img2_path).exists():
            raise FileNotFoundError(f'{img2_path}')
        self.img1 = cv2.imread(img1_path, cv2.IMREAD_UNCHANGED)
        self.img2 = cv2.imread(img2_path, cv2.IMREAD_UNCHANGED)

    def is_concordance(self) -> bool:
        # Returns whether two images match or not
        return np.array_equal(self.img1, self.img2)

    def calc_array_concd_rate(self) -> float:
        # Returns the match rate when two images are considered as a numerical matrix
        return np.count_nonzero(self.img1 == self.img2) / self.img1.size

    def calc_hist_concd_rate(self) -> float:
        # Returns the color distribution (histogram) matching rate of two images
        img1_hist = cv2.calcHist([self.img1], [0], None, [256], [0, 256])
        img2_hist = cv2.calcHist([self.img2], [0], None, [256], [0, 256])
        return cv2.compareHist(img1_hist, img2_hist, 0)

    def calc_psnr(self, *, method='skimage') -> float:
        # Returns PSNR of two images
        if method == 'cv2':
            return cv2.PSNR(self.img1, self.img2)
        else:
            return psnr(self.img1, self.img2)

    def calc_ssim(self) -> float:
        # Returns the Structural SIMilarity index (SSIM) of two images
        img_max = max(self.img1.max(), self.img2.max())
        img_min = min(self.img1.min(), self.img2.min())
        ch_axis = self.img1.shape[2] - 1
        return ssim(self.img1, self.img2, data_range=img_max - img_min, channel_axis=ch_axis)


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--img1_path', type=str, required=True, help='File path of the first target image')
    parser.add_argument('--img2_path', type=str, required=True, help='File path of the second target image')
    args = parser.parse_args()
    ica = ImgsConcdAnalyzer(args.img1_path, args.img2_path)
    print(f'Image match: {ica.is_concordance()}')
    print(f'Matrix matching rate: {ica.calc_array_concd_rate()}')
    print(f'Histgram matching rate: {ica.calc_hist_concd_rate()}')
    print(f'PSNR[dB]: {ica.calc_psnr()}')
    print(f'PSNR(OpenCV)[dB](low reliability): {ica.calc_psnr(method="cv2")}')
    print(f'SSIM: {ica.calc_ssim()}')
