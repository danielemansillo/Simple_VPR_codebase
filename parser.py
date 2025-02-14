
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # Training parameters
    parser.add_argument("--batch_size", type=int, default=64,
                        help="The number of places to use per iteration (one place is N images)")
    parser.add_argument("--img_per_place", type=int, default=4,
                        help="The effective batch size is (batch_size * img_per_place)")
    parser.add_argument("--min_img_per_place", type=int, default=4,
                        help="places with less than min_img_per_place are removed")
    parser.add_argument("--max_epochs", type=int, default=20,
                        help="stop when training reaches max_epochs")
    parser.add_argument("--num_workers", type=int, default=8,
                        help="number of processes to use for data loading / preprocessing")

    # Architecture parameters
    parser.add_argument("--descriptors_dim", type=int, default=512,
                        help="dimensionality of the output descriptors")
    
    # Visualizations parameters
    parser.add_argument("--num_preds_to_save", type=int, default=0,
                        help="At the end of training, save N preds for each query. "
                        "Try with a small number like 3")
    parser.add_argument("--save_only_wrong_preds", action="store_true",
                        help="When saving preds (if num_preds_to_save != 0) save only "
                        "preds for difficult queries, i.e. with uncorrect first prediction")

    # Paths parameters
    parser.add_argument("--train_path", type=str, default="data/gsv_xs/train",
                        help="path to train set")
    parser.add_argument("--val_path", type=str, default="data/sf_xs/val",
                        help="path to val set (must contain database and queries)")
    parser.add_argument("--test_path", type=str, default="data/sf_xs/test",
                        help="path to test set (must contain database and queries)")
    
    # NEW ARGS

    # Experiment name
    parser.add_argument("--exp_name", type=str, default="default",
                        help="exp name")

    # Checkpoint (.ckpt) file path
    parser.add_argument("--ckpt_path", type=str,
                        help="path to the checkpoint (.ckpt) file that contains the pre-trained model")

    # Loss parameter
    parser.add_argument("--loss_name", type=str, default="MultiSimilarityLoss",
                        help="loss_name among the ones specified in utils/losses.py")
    
    # Miner parameters
    parser.add_argument("--miner_name", type=str, default="MultiSimilarityMiner",
                        help="miner_name among the ones specified in utils/losses.py")
    parser.add_argument("--miner_margin", type=float, default=0.1,
                        help="miner_margin among the ones specified in utils/losses.py")
    
    # Aggregator parameters
    parser.add_argument("--agg_arch", type=str, default="ConvAP",
                        help="agg_arch among the ones specified in models/aggregators/")

    args = parser.parse_args()
    return args

