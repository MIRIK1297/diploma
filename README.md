# diploma
Bachelor's thesis, St. Petersburg State University.

An implementation of algorithm for generating images from brain signals based on Brain2Image study and Emotiv EPOC+ helmet

## Requirements

- [Emotiv EPOC+](https://www.emotiv.com/epoc/) EEG headset
- Python 3.8+
- [CyKit](https://github.com/CymatiCorp/CyKit)

## Usage

1. `pip install -r requirements.txt`
2. Obtain images from ImageNet by running get_images.ipynb notebook
3. Record EEG data: 1. run CyKit recording
                    2. run run_pics.py
                    3. stop CyKit recording
4. Run data_preparation.ipynb to slice your EEG data
5. Run encoder_final.ipybn to train encoder
6. Run gan_final.ipybn to train gan
