!python -m open_clip_train.main \
  --train-data train_small.csv \
  --val-data val_small.csv \
  --dataset-type csv \
  --csv-separator "," \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-L-14-336 \
  --pretrained openai \
  --batch-size 2 \
  --accum-freq 8 \
  --lr 5e-6 \
  --epochs 1 \
  --workers 2 \
  --precision amp \
  --logs logs_smoke

!python -m open_clip_train.main \
  --train-data train.csv \
  --val-data val.csv \
  --dataset-type csv \
  --csv-separator "," \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-L-14-336 \
  --pretrained openai \
  --batch-size 2 \
  --accum-freq 8 \
  --lr 5e-6 \
  --epochs 3 \
  --workers 2 \
  --precision amp \
  --logs logs_ssg


!python -m open_clip_train.main \
  --train-data /content/train.csv \
  --val-data /content/val.csv \
  --dataset-type csv \
  --csv-separator "," \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-L-14-336 \
  --pretrained openai \
  --batch-size 2 \
  --accum-freq 8 \
  --lr 5e-6 \
  --epochs 3 \
  --workers 2 \
  --precision amp \
  --logs logs_ssg