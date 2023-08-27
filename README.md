# Image Edge Detection using Fuzzy Inference

## Fuzzy Logic Controller
<p align="center">
<img src="https://github.com/MargiPandya27/Image-Edge-Detection-using-Fuzzy-Inference/assets/117746681/f8229ebd-b4b1-464d-abe9-9655f548e451">
</p>

## Features
* FIS approach considers the imprecision and vagueness of image features, making it an optimal solution for edge detection. 
* Traditional filter-based methods, such as the Sobel, Prewitt, and Roberts operators, rely on the same filter values to determine the presence of an edge.
* FIS controller is easily understandable.
* Fuzzy Logic algorithms can be coded using less data, so they do not occupy a huge memory space


## Comparison
<p align="center">
  <img src="https://github.com/MargiPandya27/Image-Edge-Detection-using-Fuzzy-Inference/assets/117746681/1c0855f7-bd1e-4af9-92b5-f39863c144fa">
</p>

(a) Original Test Image; Edges detected using (b) Sobel’s filter (c) Robert’s filter (d) Prewitt’s filter (e) Canny Edge Detector (f) Fuzzy Logic Controller

## Results
Result obtained by varying hyperparameters
<p align="center">
  <img src="https://github.com/MargiPandya27/Image-Edge-Detection-using-Fuzzy-Inference/assets/117746681/5eb212eb-6af5-4f0f-a176-f898ac2ecffa">
</p>
(a) Original Test Image, Image edges detected for different values of defuzzification parameter,α (b) α=0.9 and (c) α =0.6

### Application for MRI Medical Images of Brain
<p align="center">
  <img src="https://github.com/MargiPandya27/Image-Edge-Detection-using-Fuzzy-Inference/assets/117746681/26a7e849-d822-4a78-8465-8539061dac71">
</p>
(a) MRI Image of Brain with Tumor (b) Edge detection of Tumor using Python (c) Edge detection of Tumor using MATLAB

## Download images:
Download image from this site.
https://cdn.pixabay.com/photo/2016/01/08/05/24/sunflower-1127174__340.jpg

## Requirements
* Python Version >3.0
  
### Libraries used:
* `cv2`
* `numpy` 
* `math`
* `pandas` 
* `matplotlib.pyplot`

### Citation
If you found our model useful in your research, please consider starring ⭐ us on GitHub and citing 📚 us in your research!

```bibtex
@INPROCEEDINGS{10150762,
  author={Pandey, Aman Kumar and Chatla, H R S S Nagavalli and Pandya, Margi and Farhan M A, Aneesa and Rana, Ankur Singh},
  booktitle={2023 International Conference on Recent Advances in Electrical, Electronics & Digital Healthcare Technologies (REEDCON)}, 
  title={Image Edge Detection Using Fuzzy Logic Controller}, 
  year={2023},
  volume={},
  number={},
  pages={508-513},
  doi={10.1109/REEDCON57544.2023.10150762}}
```


