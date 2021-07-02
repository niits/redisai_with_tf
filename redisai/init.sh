cat exported/resnet50.pb | redis-cli -x AI.MODELSTORE imagenet_model TF CPU TAG imagenet:5.0 INPUTS 1 images OUTPUTS 1 output BLOB

cat data_processing_script.py | redis-cli -x AI.SCRIPTSET imagenet_script CPU TAG imagenet_script:v0.1 SOURCE