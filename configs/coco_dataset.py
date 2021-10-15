pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]

dataset = dict(
    type='CocoDataset',
    ann_file=data_root + 'annotations/instances_train2017.json',
    img_prefix=data_root + 'train2017/',
    pipeline=train_pipeline),
