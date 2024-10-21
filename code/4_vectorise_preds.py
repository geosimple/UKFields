from osgeo import gdal
gdal.SetConfigOption('GDAL_VRT_ENABLE_PYTHON', 'YES')
gdal.UseExceptions()

from utils import setup_environment, get_vrt_metadata, generate_contours, merge_contours
from sys import argv

path_root=argv[2]

if __name__ == "__main__":
    out_name = f'{path_root}/demo.vrt'
    pred_dir = argv[1] #"/home/eesjb/Documents/segment-anything/segment-anything-eo/predictions/utm27700"
    weight_file = f'{path_root}/weights.tif'
    shape = (1024, 1024)
    buffer = 128
    contours_dir = argv[3] #'contours'
    output_file = f'{path_root}/merged.gpkg'

    setup_environment(out_name, pred_dir, weight_file, shape, buffer, path_root)
    meta, vrt_dim, transform = get_vrt_metadata(out_name)
    #if large vrt file, run on high memory machine
    generate_contours(out_name, vrt_dim, buffer, contours_dir, path_root)
    merge_contours(vrt_dim, buffer, contours_dir, output_file, path_root)
