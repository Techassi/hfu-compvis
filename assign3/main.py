# External packages
import click

import cmd.features as features
import cmd.rectify as rectify
import cmd.matrix as matrix
import cmd.dmap as dmap

# Intrinsische Matrix aus EXIF Daten
# Fundamental Matrix erstellen
# Rektifizieren
# Stereo Algos anwenden
# Depth map


@click.group()
def cli():
    pass


@cli.group('features')
def features_group():
    '''
    Detect various features in images.
    '''
    pass


@cli.group('dmap')
def map_group():
    '''
    Compute depth maps.
    '''
    pass


@cli.command('matrix')
@click.option('-p', '--path', default='.data', help='Path to source images', type=str, show_default=True)
def matrix_cmd(path: str):
    '''
    Calculate the intrinsic camera matrix.
    '''
    matrix.execute(path)


@cli.command('rectify')
@click.option('-p', '--path', default='.data', help='Path to source images', type=str, show_default=True)
@click.option('-t', '--thresh', default=0, help='Threshold to filter out outliers', type=int, show_default=True)
@click.option('--preview', default=False, help='Show preview windows', type=bool, is_flag=True)
def rectify_cmd(path: str, preview: bool, thresh: int):
    '''
    Rectify two or more images.
    '''
    rectify.execute(path, preview, thresh)


@features_group.command('lines')
@click.option('-p', '--path', default='.data', help='Path to source images', type=str, show_default=True)
@click.option('--preview', default=False, help='Show preview windows', type=bool, is_flag=True)
def epilines_cmd(path: str, preview: bool):
    '''
    Extract epipolar lines from two or more images.
    '''
    features.epilines(path, preview)


@features_group.command('points')
@click.option('-p', '--path', default='.data', help='Path to source images', type=str, show_default=True)
@click.option('--preview', default=False, help='Show preview windows', type=bool, is_flag=True)
def points_cmd(path: str, preview: bool):
    '''
    Extract matching feature points.
    '''
    features.points(path, preview)


@map_group.command('single')
@click.option('-p', '--path', default='.data', help='Path to source images', type=str, show_default=True)
@click.option('--preview', default=False, help='Show preview windows', type=bool, is_flag=True)
@click.option('--speckle-size', default=10, help='Speckle window size', type=int, show_default=True)
@click.option('--speckle-range', default=8, help='Speckle range', type=int, show_default=True)
@click.option('--min-disp', default=0, help='Minimum disparity', type=int, show_default=True)
@click.option('--num-disp', default=64, help='Number of disparities', type=int, show_default=True)
@click.option('--disp-diff', default=1, help='Disparity 1-2 max diff', type=int, show_default=True)
@click.option('--unique-ratio', default=10, help='Uniqueness ratio', type=int, show_default=True)
@click.option('--block-size', default=8, help='Block size', type=int, show_default=True)
def single_map_cmd(
    path: str,
    preview: bool,
    speckle_size: int,
    speckle_range: int,
    min_disp: int,
    num_disp: int,
    disp_diff: int,
    unique_ratio: int,
    block_size: int
):
    '''
    Compute a single depth map from two images.
    '''
    dmap.single(
        path,
        preview,
        speckle_size,
        speckle_range,
        min_disp,
        num_disp,
        disp_diff,
        unique_ratio,
        block_size
    )


@map_group.command('multi')
@click.option('-p', '--path', default='.data', help='Path to source images', type=str, show_default=True)
@click.option('--preview', default=False, help='Show preview windows', type=bool, is_flag=True)
@click.option('--speckle-size', default=10, help='Speckle window size', type=int, show_default=True)
@click.option('--speckle-range', default=8, help='Speckle range', type=int, show_default=True)
@click.option('--min-disp', default=0, help='Minimum disparity', type=int, show_default=True)
@click.option('--num-disp', default=64, help='Number of disparities', type=int, show_default=True)
@click.option('--disp-diff', default=1, help='Disparity 1-2 max diff', type=int, show_default=True)
@click.option('--unique-ratio', default=10, help='Uniqueness ratio', type=int, show_default=True)
@click.option('--block-size', default=8, help='Block size', type=int, show_default=True)
def multi_map_cmd(
    path: str,
    preview: bool,
    speckle_size: int,
    speckle_range: int,
    min_disp: int,
    num_disp: int,
    disp_diff: int,
    unique_ratio: int,
    block_size: int
):
    '''
    Combine several depth maps from two images.
    '''
    dmap.multi(
        path,
        preview,
        speckle_size,
        speckle_range,
        min_disp,
        num_disp,
        disp_diff,
        unique_ratio,
        block_size
    )


@cli.command('sweep')
def sweep_cmd():
    pass


if __name__ == '__main__':
    cli()
