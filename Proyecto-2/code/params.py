
#Variables that contains the user credentials for the Twitter API 
access_token = "104997748-7cCdw06UzvQI86C5bHskKl90qCPJi3vfbRTEef68"
access_token_secret = "ojBA7ZYhqrMrv6z0MqkonY74wOfQ9WZpNFloFgHykBib9"
consumer_key = "WKtmu8QRdyTtKDeMirpDW50zj"
consumer_secret = "G3pP3ZLJBcE7AHhiGAOsLPy06956oXUCbGstp0OIKM8EEH7312"

#destination folder for raw tweets 
folder_path = "raw/"
#destination folder for clean tweets
clean_path = "clean/"
#name of file to store tweets
tweetFilename = "tweets"
tweetFilename = tweetFilename + ".json"

# the list of tracking words 
"""
tracklist = {
'@luchocastanedap': ['@luchocastanedap', 'luis castañeda',  'Luis Castañeda Pardo'],
'@DanielUrresti1': ['@DanielUrresti1', 'Daniel Urresti'],
'@humberto_lay': ['@humberto_lay', 'Humberto Lay', 'Humberto Lay Sun'],
'@RicardoBelmontC': ['@RicardoBelmontC', 'Ricardo Belmont', 'Ricardo Belmont Cassinelli'],
'@BeingoleaA': ['@BeingoleaA', 'Alberto Beingolea'],
'@jaimesalinas80': ['@jaimesalinas80', 'Jaime Salinas'],
'@JorgeMunozAP': ['@JorgeMunozAP', 'Jorge Muñoz', 'Jorge Muñoz Wells'],
'@EstherCapunay': ['@EstherCapunay', 'Esther Capuñay', 'La Capuñay'],
'@ManuelVelardeD': ['@ManuelVelardeD', 'Manuel Velarde'],
'@DitelColumbus': ['@DitelColumbus', 'Ditel Columbus', 'Ditel Columbus - LIMA'],
'@ENRIQUECORNEJOR': ['@ENRIQUECORNEJOR', 'Enrique Cornejo'],
'@juancarloszurek': ['@juancarloszurek', 'Juan Carlos Zurek'],
'@JulioGagoPe': ['@JulioGagoPe', 'Julio Gagó Pérez', 'Julio Gagó'],
'@Renzo_Reggiardo': ['@Renzo_Reggiardo', 'Renzo Reggiardo'],
'@EnriquePorLima': ['@EnriquePorLima', 'Enrique Fernández Chacón'],
'@kikeocrospoma': ['@kikeocrospoma', 'Enrique Ocrospoma'],
'@GGG_pe': ['@GGG_pe', 'Gustavo Guerra García'],
'@GomezBacaxLima': ['@GomezBacaxLima', 'Roberto Gómez Baca']
}
"""

tracklist = {
    'Lapadula':['Gianluca Lapadula', 'Lapadula', 'lapadula', '@G_Lapadula'],
    'Gareca':['Ricardo Gareca', 'Gareca', 'gareca'],
    'Gallese':['Pedro Gallese', 'Gallese', 'gallese', '@pedrogallese'],
    'Guerrero':['Paolo Guerrero', 'Guerrero', 'guerrero', '@PaoloGuerreroOf'],
    'Cueva':['Christian Cueva', 'Cueva', 'cueva', '@Cuevachris10'],
    'Tapia':['Renato Tapia', 'Tapia', 'tapia', '@renatotapiac'],
    'Trauco':['Miguel Trauco', 'Trauco', 'trauco', '@mtrauco17'],
    'Ramos':['Christian Ramos', 'Ramos', 'ramos', '@RamosGaragay'],
    'Corzo':['Aldo Corzo', 'Corzo', 'corzo', '@Alditocorzo'],
    'Copa America':['Copa América', 'copa america', 'copa america 2021', 'Copa America 2021', '#CopaAmérica']
}
