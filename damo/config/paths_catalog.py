# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# Copyright (C) Alibaba Group Holding Limited. All rights reserved.
"""Centralized catalog of paths."""
import os


class DatasetCatalog(object):
    DATA_DIR = 'datasets'
    DATASETS = {
        'coco_train': {
            'img_dir': 'coco/images',
            'ann_file': 'coco/annotations/train.json'
        },
        'coco_val': {
            'img_dir': 'coco/images',
            'ann_file': 'coco/annotations/val.json'
        },
        }

    @staticmethod
    def get(name):
        if 'coco' in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                root=os.path.join(data_dir, attrs['img_dir']),
                ann_file=os.path.join(data_dir, attrs['ann_file']),
            )
            return dict(
                factory='COCODataset',
                args=args,
            )
        else:
            raise RuntimeError('Only support coco format now!')
        return None
