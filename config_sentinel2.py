# ARQUIVO DE CONFIGURACAO PARA EXPORTAR IMAGENS SENTINEL 2
# PARA O GOOGLE DRIVE, UTLIZANDO O GOOGLE EARTH ENGINE.

# DATAS
# start_date - data inicial para procurar imagens
# exemplo: start_date = '2013-05-01'
start_date = '2013-05-01'
# end_date - ultima data para procurar imagens
# exemplo: end_date = '2018-12-01'
end_date = '2018-12-01'
# OBS: (I) end_date pode ser uma data que ainda nao aconteceu
#      (II) datas impossiveis nao funcionam, e.g, '2018-05-31'


# TAMANHO DO PIXEL
# tamanho que o pixel da imagem de saida vai ter
# exemplo: scale = 20
scale = 20

# TILES SENTINEL
# tiles para serem exportados
# os possiveis valores sao:
# uma lista de strings: ['granule1','granule2',...,'granuleN']*
# ou None, ver **
# # exemplo: tiles = [
# #     '23KPT',
# #     '23KPU',
# #     '23KQT',
# #     '23KQU'
# # ]
tiles = None
# tiles = [
#     '23KPT',
#     '23KPU',
#     '23KQT',
#     '23KQU'
# ]
# caso se saiba apriori quais imagens devem ser exportadas,
# as imagens podem ser informadas como um lista de strings ver *
# note que se 'images' e 'tiles' sao mutualmente exclusivos**.
# entao se tiles for uma lista de strings, entao images=None
# ou vice e versa, caso contrario teremos um erro.
# exemplo: images = [
#     'COPERNICUS/S2/20160713T130431_20160713T192011_T23KPT',
#     'COPERNICUS/S2/20160713T130431_20160713T192011_T23KPU'
# ] ou images = None
images = [
    'COPERNICUS/S2/20160616T131245_20160616T193218_T23KNR',
    'COPERNICUS/S2/20160713T130431_20160713T192011_T23KNR',
    'COPERNICUS/S2/20170830T131241_20170830T131242_T23KNR',
    'COPERNICUS/S2/20170906T130251_20170906T130246_T23KNR',
    'COPERNICUS/S2/20180522T131239_20180522T131330_T23KNR',
    'COPERNICUS/S2/20160713T130431_20160713T192011_T23KQR',
    'COPERNICUS/S2/20170906T130251_20170906T130246_T23KQR',
    'COPERNICUS/S2/20180119T130239_20180119T130239_T23KQR',
    'COPERNICUS/S2/20160802T130656_20160802T193908_T23KQS',
    'COPERNICUS/S2/20170906T130251_20170906T130246_T23KQS',
    'COPERNICUS/S2/20180119T130239_20180119T130239_T23KQS',
    'COPERNICUS/S2/20160713T130431_20160713T192011_T23KPR',
    'COPERNICUS/S2/20171011T130229_20171011T130232_T23KPR',
    'COPERNICUS/S2/20160424T130240_20160424T181611_T23KNQ',
    'COPERNICUS/S2/20160706T131549_20160706T194917_T23KNQ',
    'COPERNICUS/S2/20170618T130251_20170618T130604_T23KNQ',
    'COPERNICUS/S2/20170721T131241_20170721T131244_T23KNQ',
    'COPERNICUS/S2/20180325T130251_20180325T130245_T23KNQ',
    'COPERNICUS/S2/20180522T131239_20180522T131330_T23KNQ',
    'COPERNICUS/S2/20160616T131245_20160616T193218_T23KMR',
    'COPERNICUS/S2/20170830T131241_20170830T131242_T23KMR',
    'COPERNICUS/S2/20180522T131239_20180522T131330_T23KMR',
    'COPERNICUS/S2/20160616T131245_20160616T193218_T23KMQ',
    'COPERNICUS/S2/20170830T131241_20170830T131242_T23KMQ',
    'COPERNICUS/S2/20180522T131239_20180522T131330_T23KMQ',
    'COPERNICUS/S2/20150801T131806_20160820T091120_T23KMP',
    'COPERNICUS/S2/20160706T131549_20160706T194917_T23KMP',
    'COPERNICUS/S2/20170611T131241_20170611T131243_T23KMP',
    'COPERNICUS/S2/20180522T131239_20180522T131330_T23KMP',
    'COPERNICUS/S2/20160713T130431_20160713T192011_T23KPS',
    'COPERNICUS/S2/20170906T130251_20170906T130246_T23KPS',
    'COPERNICUS/S2/20180119T130239_20180119T130239_T23KPS',
    'COPERNICUS/S2/20160616T131245_20160616T193218_T23KNS',
    'COPERNICUS/S2/20160713T130431_20160713T192011_T23KNS',
    'COPERNICUS/S2/20170830T131241_20170830T131242_T23KNS',
    'COPERNICUS/S2/20170904T131239_20170904T131236_T23KNS',
    'COPERNICUS/S2/20180522T131239_20180522T131330_T23KNS',
]
# images = None

# GEOMETRIA
# geometria para cortar todos os tiles, polygon nao multipolygons
# se geometry=None, entao o tile inteiro sera exportado
# exemplo: geometry = 'users/cnp_rafael/buffer_50km'
# geometry = 'users/cnp_rafael/buffer_50km'
geometry = 'users/leon_cnp/buff_3km'
# GEOMETRY BUFFER
# geometry_buff = 5000
geometry_buff = None

# PASTA DE SAIDA
# nome da pasta para qual as imagens vao ser exportadas
# exemplo: folder_name = 'sao_domingos_do_prata'
folder = 'portos_roi_31983'

# CRS
# codigo EPSG (escrever EPSG maiusculo), ver http://spatialreference.org/
# exemplo: crs = 'EPSG:4326'
crs = 'EPSG:31983'

# DESIRED BANDS
# informe as bandas desejadas no formato de lista de strings ver *
# ver https://landsat.gsfc.nasa.gov/sentinel-2a-launches-our-compliments-our-complements/
# exemplo: desired_bands = ['B8A', 'B11', 'B4']
desired_bands = ['B8A', 'B11', 'B4']


# BANDA DE QUALIDADE
# Se true, a banda de qualidade no formato binario tambem vai ser exportada
# qa = True
qa = False
