#!/bin/sh

#Install all dependencies required

#this link for conda
#https://docs.conda.io/en/latest/miniconda.html?ref=learn-ubuntu#linux-installers

conda install -c huggingface transformers

conda install pytorch torchvision -c soumith