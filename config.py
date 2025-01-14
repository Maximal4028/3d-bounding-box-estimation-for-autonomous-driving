import os
class config():
    def __init__(self):
        # Todo: set base_dir to kitti/image_2
        self.base_dir = '/home/old_repo/data/kitti_dataset'
        #self.base_dir = '/mnt/niosrv/DataSets/benchmarks/kitti/kitti_2011_09_26_drive_0084/kitti_dataset'

        # Todo: set the base network: vgg16, vgg16_conv or mobilenet_v2
        self.network = 'mobilenet_v2'

        # set the bin size
        self.bin = 2

        # set the train/val split
        self.split = 0.8

        # set overlapping
        self.overlap = 0.1

        # set jittered
        self.jit = 3

        # set the normalized image size
        self.norm_w = 224
        self.norm_h = 224

        # set the batch size
        self.batch_size = 8

        # set the categories
        #self.KITTI_cat = ['Car', 'Cyclist', 'Pedestrian']
        self.KITTI_cat = ['Car', 'Pedestrian']
        # self.KITTI_cat = ['Car']
