import streamlit as st
import pandas as pd
import joblib 

st.set_page_config(
    page_title="Cars",
    page_icon="🚗")

## LOAD MODEL ##
@st.cache_resource
def load_pipe():
    return joblib.load('model.pkl')

pipe = load_pipe()

## INPUT FROM USER  ##
st.sidebar.header("Car Pirce Predictions App")


Engine_HP = st.sidebar.number_input(
    "Engine HP",
    min_value=1,
    value=2000
)

Engine_Cylinders = st.sidebar.number_input(
    "Engine Cylinders",
    min_value=1,
    value=400
)


Popularity = st.sidebar.number_input(
    "Popularity",
    min_value=1,
    value=350
)

year = st.sidebar.number_input(
    "Year",
    min_value=1,
    value=350
)


Transmission_Type  = st.sidebar.selectbox(
    "Transmission Type",
    [ 
        'AUTOMATIC',
        'MANUAL',             
        'AUTOMATED_MANUAL',  
        'DIRECT_DRIVE',         
        'UNKNOWN'
    ]
)

Make = st.sidebar.selectbox(
    "Make" , 
    [
    'BMW', 'Audi', 'FIAT', 'Mercedes-Benz', 'Chrysler', 'Nissan',
    'Volvo', 'Mazda', 'Mitsubishi', 'Ferrari', 'Alfa Romeo', 'Toyota',
    'McLaren', 'Maybach', 'Pontiac', 'Porsche', 'Saab', 'GMC',
    'Hyundai', 'Plymouth', 'Honda', 'Oldsmobile', 'Suzuki', 'Ford',
    'Cadillac', 'Kia', 'Bentley', 'Chevrolet', 'Dodge', 'Lamborghini',
    'Lincoln', 'Subaru', 'Volkswagen', 'Spyker', 'Buick', 'Acura',
    'Rolls-Royce', 'Maserati', 'Lexus', 'Aston Martin', 'Land Rover',
    'Lotus', 'Infiniti', 'Scion', 'Genesis', 'HUMMER', 'Tesla',
    'Bugatti'])

Model= st.sidebar.selectbox(
    "Model" , 
   ['1 Series M', '1 Series', '100', '124 Spider', '190-Class',
       '2 Series', '200', '200SX', '240SX', '240', '2',
       '3 Series Gran Turismo', '3 Series', '300-Class', '3000GT', '300',
       '300M', '300ZX', '323', '350-Class', '350Z', '360', '370Z', '3',
       '4 Series Gran Coupe', '4 Series', '400-Class', '420-Class',
       '456M', '458 Italia', '4C', '4Runner', '5 Series Gran Turismo',
       '5 Series', '500-Class', '500e', '500', '500L', '500X', '550',
       '560-Class', '570S', '575M', '57', '599', '5',
       '6 Series Gran Coupe', '6 Series', '600-Class', '6000',
       '612 Scaglietti', '626', '62', '650S Coupe', '650S Spider', '6',
       '7 Series', '718 Cayman', '740', '760', '780', '8 Series', '80',
       '850', '86', '9-2X', '9-3 Griffin', '9-3', '9-4X', '9-5', '9-7X',
       '9000', '900', '90', '911', '928', '929', '940', '944', '960',
       '968', 'A3', 'A4 allroad', 'A4', 'A5', 'A6', 'A7', 'A8',
       'Acadia Limited', 'Acadia', 'Accent', 'Acclaim',
       'Accord Crosstour', 'Accord Hybrid', 'Accord Plug-In Hybrid',
       'Accord', 'Achieva', 'ActiveHybrid 5', 'ActiveHybrid 7',
       'ActiveHybrid X6', 'Aerio', 'Aerostar', 'Alero', 'Allante',
       'allroad quattro', 'allroad', 'ALPINA B6 Gran Coupe', 'ALPINA B7',
       'Alpina', 'Altima Hybrid', 'Altima', 'Amanti', 'AMG GT', 'Armada',
       'Arnage', 'Aspen', 'Aspire', 'Astro Cargo', 'Astro', 'ATS Coupe',
       'ATS-V', 'ATS', 'Aurora', 'Avalanche', 'Avalon Hybrid', 'Avalon',
       'Avenger', 'Aventador', 'Aveo', 'Aviator', 'Axxess', 'Azera',
       'Aztek', 'Azure T', 'Azure', 'B-Class Electric Drive',
       'B-Series Pickup', 'B-Series Truck', 'B-Series', 'B9 Tribeca',
       'Baja', 'Beetle Convertible', 'Beetle', 'Beretta',
       'Black Diamond Avalanche', 'Blackwood', 'Blazer', 'Bolt EV',
       'Bonneville', 'Borrego', 'Boxster', 'Bravada', 'Breeze',
       'Bronco II', 'Bronco', 'Brooklands', 'Brougham', 'BRZ', 'C-Class',
       'C-Max Hybrid', 'C30', 'C36 AMG', 'C43 AMG', 'C70', 'C8',
       'Cabriolet', 'Cabrio', 'Cadenza', 'Caliber', 'California T',
       'California', 'Camaro', 'Camry Hybrid', 'Camry Solara', 'Camry',
       'Canyon', 'Caprice', 'Captiva Sport', 'Caravan', 'Carrera GT',
       'Cascada', 'Catera', 'Cavalier', 'Cayenne', 'Cayman S', 'Cayman',
       'CC', 'Celebrity', 'Celica', 'Century', 'Challenger', 'Charger',
       'Chevy Van', 'Ciera', 'Cirrus', 'City Express', 'Civic CRX',
       'Civic del Sol', 'Civic', 'C/K 1500 Series', 'C/K 2500 Series',
       'CL-Class', 'CLA-Class', 'CL', 'Classic', 'CLK-Class', 'CLS-Class',
       'Cobalt', 'Colorado', 'Colt', 'Concorde',
       'Continental Flying Spur Speed', 'Continental Flying Spur',
       'Continental GT Speed Convertible', 'Continental GT Speed',
       'Continental GT3-R', 'Continental GT', 'Continental GTC Speed',
       'Continental GTC', 'Continental Supersports Convertible',
       'Continental Supersports', 'Continental', 'Contour SVT', 'Contour',
       'Corniche', 'Corolla iM', 'Corolla', 'Corrado', 'Corsica',
       'Corvette Stingray', 'Corvette', 'Coupe', 'CR-V', 'CR-Z',
       'Cressida', 'Crossfire', 'Crosstour', 'Crosstrek',
       'Crown Victoria', 'Cruze Limited', 'Cruze', 'CT 200h', 'CT6',
       'CTS Coupe', 'CTS-V Coupe', 'CTS-V Wagon', 'CTS-V', 'CTS Wagon',
       'CTS', 'Cube', 'Custom Cruiser', 'Cutlass Calais', 'Cutlass Ciera',
       'Cutlass Supreme', 'Cutlass', 'CX-3', 'CX-5', 'CX-7', 'CX-9',
       'Dakota', 'Dart', 'Dawn', 'Daytona', 'DB7', 'DB9 GT', 'DB9', 'DBS',
       'Defender', 'DeVille', 'Diablo', 'Diamante', 'Discovery Series II',
       'Discovery Sport', 'Discovery', 'DTS', 'Durango', 'Dynasty',
       'E-150', 'E-250', 'E-Class', 'e-Golf', 'E-Series Van',
       'E-Series Wagon', 'E55 AMG', 'ECHO', 'Eclipse Spyder', 'Eclipse',
       'Edge', 'Eighty-Eight Royale', 'Eighty-Eight', 'Elantra Coupe',
       'Elantra GT', 'Elantra Touring', 'Elantra', 'Eldorado', 'Electra',
       'Element', 'Elise', 'Enclave', 'Encore', 'Endeavor', 'Entourage',
       'Envision', 'Envoy XL', 'Envoy XUV', 'Envoy', 'Enzo', 'Eos',
       'Equator', 'Equinox', 'Equus', 'ES 250', 'ES 300h', 'ES 300',
       'ES 330', 'ES 350', 'Escalade ESV', 'Escalade EXT',
       'Escalade Hybrid', 'Escalade', 'Escape Hybrid', 'Escape', 'Escort',
       'Esprit', 'Estate Wagon', 'Esteem', 'EuroVan', 'Evora 400',
       'Evora', 'EX35', 'Excel', 'Exige', 'EX', 'Expedition',
       'Explorer Sport Trac', 'Explorer Sport', 'Explorer', 'Expo',
       'Express Cargo', 'Express', 'F-150 Heritage',
       'F-150 SVT Lightning', 'F-150', 'F-250', 'F12 Berlinetta', 'F430',
       'Festiva', 'FF', 'Fiesta', 'Firebird', 'Fit EV', 'Fit',
       'Five Hundred', 'FJ Cruiser', 'Fleetwood', 'Flex', 'Flying Spur',
       'Focus RS', 'Focus ST', 'Focus', 'Forenza', 'Forester', 'Forte',
       'Fox', 'FR-S', 'Freelander', 'Freestar', 'Freestyle', 'Frontier',
       'Fusion Hybrid', 'Fusion', 'FX35', 'FX45', 'FX50', 'FX', 'G-Class',
       'G Convertible', 'G Coupe', 'G Sedan', 'G20', 'G35',
       'G37 Convertible', 'G37 Coupe', 'G37 Sedan', 'G37', 'G3', 'G5',
       'G6', 'G80', 'G8', 'Galant', 'Gallardo', 'Genesis Coupe',
       'Genesis', 'Ghibli', 'Ghost Series II', 'Ghost', 'GL-Class',
       'GLA-Class', 'GLC-Class', 'GLE-Class Coupe', 'GLE-Class', 'GLI',
       'GLK-Class', 'GLS-Class', 'Golf Alltrack', 'Golf GTI', 'Golf R',
       'Golf SportWagen', 'Golf', 'Grand Am', 'Grand Caravan',
       'Grand Prix', 'Grand Vitara', 'Grand Voyager', 'GranSport',
       'GranTurismo Convertible', 'GranTurismo', 'GS 200t', 'GS 300',
       'GS 350', 'GS 400', 'GS 430', 'GS 450h', 'GS 460', 'GS F', 'GT-R',
       'GT', 'GTI', 'GTO', 'GX 460', 'GX 470', 'H3', 'H3T', 'HHR',
       'Highlander Hybrid', 'Highlander', 'Horizon', 'HR-V', 'HS 250h',
       'Huracan', 'i-MiEV', 'I30', 'I35', 'i3', 'iA', 'ILX Hybrid', 'ILX',
       'Impala Limited', 'Impala', 'Imperial', 'Impreza WRX', 'Impreza',
       'iM', 'Insight', 'Integra', 'Intrepid', 'Intrigue', 'iQ',
       'IS 200t', 'IS 250 C', 'IS 250', 'IS 300', 'IS 350 C', 'IS 350',
       'IS F', 'J30', 'Jetta GLI', 'Jetta Hybrid', 'Jetta SportWagen',
       'Jetta', 'Jimmy', 'Journey', 'Juke', 'Justy', 'JX', 'K900',
       'Kizashi', 'LaCrosse', 'Lancer Evolution', 'Lancer Sportback',
       'Lancer', 'Land Cruiser', 'Landaulet', 'Laser', 'Le Baron',
       'Le Mans', 'Leaf', 'Legacy', 'Legend', 'LeSabre', 'Levante', 'LFA',
       'LHS', 'Loyale', 'LR2', 'LR3', 'LR4', 'LS 400', 'LS 430', 'LS 460',
       'LS 600h L', 'LS', 'LSS', 'LTD Crown Victoria', 'Lucerne',
       'Lumina Minivan', 'Lumina', 'LX 450', 'LX 470', 'LX 570',
       'M-Class', 'M2', 'M30', 'M35', 'M37', 'M3', 'M4 GTS', 'M45', 'M4',
       'M56', 'M5', 'M6 Gran Coupe', 'M6', 'Macan', 'Magnum',
       'Malibu Classic', 'Malibu Hybrid', 'Malibu Limited', 'Malibu Maxx',
       'Malibu', 'Mark LT', 'Mark VIII', 'Mark VII', 'Matrix', 'Maxima',
       'Maybach', 'Mazdaspeed 3', 'Mazdaspeed 6', 'Mazdaspeed MX-5 Miata',
       'Mazdaspeed Protege', 'M', 'MDX', 'Metris', 'Metro',
       'Mighty Max Pickup', 'Millenia', 'Mirage G4', 'Mirage', 'MKC',
       'MKS', 'MKT', 'MKX', 'MKZ Hybrid', 'MKZ', 'ML55 AMG', 'Model S',
       'Monaco', 'Montana SV6', 'Montana', 'Monte Carlo', 'Montero Sport',
       'Montero', 'MP4-12C', 'MPV', 'MR2 Spyder', 'MR2', 'Mulsanne',
       'Murano CrossCabriolet', 'Murano', 'Murcielago',
       'Mustang SVT Cobra', 'Mustang', 'MX-3', 'MX-5 Miata', 'MX-6',
       'Navajo', 'Navigator', 'Neon', 'New Beetle', 'New Yorker',
       'Ninety-Eight', 'Nitro', 'NSX', 'NV200', 'NX 200t', 'NX 300h',
       'NX', 'Odyssey', 'Omni', 'Optima Hybrid', 'Optima', 'Outback',
       'Outlander Sport', 'Outlander', 'Pacifica', 'Panamera',
       'Park Avenue', 'Park Ward', 'Paseo', 'Passat', 'Passport',
       'Pathfinder', 'Phaeton', 'Phantom Coupe', 'Phantom Drophead Coupe',
       'Phantom', 'Pickup', 'Pilot', 'Precis', 'Prelude', 'Previa',
       'Prius c', 'Prius Prime', 'Prius v', 'Prius', 'Prizm', 'Probe',
       'Protege5', 'Protege', 'Prowler', 'PT Cruiser', 'Pulsar', 'Q3',
       'Q40', 'Q45', 'Q50', 'Q5', 'Q60 Convertible', 'Q60 Coupe', 'Q70',
       'Q7', 'Quattroporte', 'Quest', 'QX4', 'QX50', 'QX56', 'QX60',
       'QX70', 'QX80', 'QX', 'R-Class', 'R32', 'R8', 'Rabbit', 'Raider',
       'Rainier', 'Rally Wagon', 'RAM 150', 'RAM 250', 'Ram 50 Pickup',
       'Ram Cargo', 'Ram Pickup 1500', 'Ram Van', 'Ram Wagon',
       'Ramcharger', 'Range Rover Evoque', 'Range Rover Sport',
       'Range Rover', 'Ranger', 'Rapide S', 'Rapide', 'RAV4 EV',
       'RAV4 Hybrid', 'RAV4', 'RC 200t', 'RC 300', 'RC 350', 'RC F',
       'RDX', 'Reatta', 'Regal', 'Regency', 'Rendezvous', 'Reno',
       'Reventon', 'Ridgeline', 'Rio', 'Riviera', 'RL', 'RLX',
       'Roadmaster', 'Rogue Select', 'Rogue', 'Rondo', 'Routan', 'RS 4',
       'RS 5', 'RS 6', 'RS 7', 'RSX', 'RX 300', 'RX 330', 'RX 350',
       'RX 400h', 'RX 450h', 'RX-7', 'RX-8', 'S-10 Blazer', 'S-10',
       'S-15 Jimmy', 'S-15', 'S-Class', 'S2000', 'S3', 'S40', 'S4', 'S5',
       'S60 Cross Country', 'S60', 'S6', 'S70', 'S7', 'S80', 'S8', 'S90',
       'Safari Cargo', 'Safari', 'Samurai', 'Santa Fe Sport', 'Santa Fe',
       'Savana Cargo', 'Savana', 'SC 300', 'SC 400', 'SC 430', 'Scoupe',
       'Sebring', 'Sedona', 'Sentra', 'Sephia', 'Sequoia', 'Seville',
       'Shadow', 'Shelby GT350', 'Shelby GT500', 'Sidekick', 'Sienna',
       'Sierra 1500 Classic', 'Sierra 1500 Hybrid', 'Sierra 1500',
       'Sierra 1500HD', 'Sierra C3', 'Sierra Classic 1500', 'Sigma',
       'Silhouette', 'Silver Seraph', 'Silverado 1500 Classic',
       'Silverado 1500 Hybrid', 'Silverado 1500', 'Sixty Special',
       'Skylark', 'SL-Class', 'SLC-Class', 'SLK-Class', 'SLR McLaren',
       'SLS AMG GT Final Edition', 'SLS AMG GT', 'SLS AMG', 'SLX',
       'Solstice', 'Sonata Hybrid', 'Sonata', 'Sonic', 'Sonoma',
       'Sorento', 'Soul EV', 'Soul', 'Spark EV', 'Spark', 'Spectra',
       'Spirit', 'Sportage', 'Sportvan', 'Spyder', 'SQ5', 'SRT Viper',
       'SRX', 'SS', 'SSR', 'Stanza', 'Stealth', 'Stratus', 'STS-V', 'STS',
       'Suburban', 'Sunbird', 'Sundance', 'Sunfire', 'Superamerica',
       'Supersports Convertible ISR', 'Supra', 'SVX', 'Swift', 'SX4',
       'Syclone', 'T100', 'Tacoma', 'Tahoe Hybrid', 'Tahoe Limited/Z71',
       'Tahoe', 'Taurus X', 'Taurus', 'TC', 'tC', 'Tempo', 'Tercel',
       'Terrain', 'Terraza', 'Thunderbird', 'Tiburon', 'Tiguan', 'Titan',
       'TL', 'TLX', 'Toronado', 'Torrent', 'Touareg 2', 'Touareg',
       'Town and Country', 'Town Car', 'Tracker', 'TrailBlazer EXT',
       'TrailBlazer', 'Trans Sport', 'Transit Connect', 'Transit Wagon',
       'Traverse', 'Trax', 'Tribeca', 'Tribute Hybrid', 'Tribute',
       'Truck', 'TSX Sport Wagon', 'TSX', 'TT RS', 'TT', 'TTS', 'Tucson',
       'Tundra', 'Typhoon', 'Uplander', 'V12 Vanquish', 'V12 Vantage S',
       'V12 Vantage', 'V40', 'V50', 'V60 Cross Country', 'V60', 'V70',
       'V8 Vantage', 'V8', 'V90', 'Vanagon', 'Vandura', 'Van', 'Vanquish',
       'Vanwagon', 'Veloster', 'Venture', 'Venza', 'Veracruz', 'Verano',
       'Verona', 'Versa Note', 'Versa', 'Veyron 16.4', 'Vibe', 'Vigor',
       'Viper', 'Virage', 'Vitara', 'Voyager', 'Windstar Cargo',
       'Windstar', 'Wraith', 'WRX', 'X-90', 'X1', 'X3', 'X4', 'X5 M',
       'X5', 'X6 M', 'X6', 'xA', 'xB', 'XC60', 'XC70', 'XC90', 'XC', 'xD',
       'XG300', 'XG350', 'XL-7', 'XL7', 'XLR-V', 'XLR', 'XT5', 'Xterra',
       'XTS', 'XT', 'XV Crosstrek', 'Yaris iA', 'Yaris', 'Yukon Denali',
       'Yukon Hybrid', 'Yukon XL', 'Yukon', 'Z3', 'Z4 M', 'Z4', 'Z8',
       'ZDX', 'Zephyr'])

Engine_Fuel_Type = st.sidebar.selectbox(
    "Engine Fuel Type" ,  
    ['premium unleaded (required)', 'regular unleaded',
       'premium unleaded (recommended)', 'flex-fuel (unleaded/E85)',
       'diesel', 'electric',
       'flex-fuel (premium unleaded recommended/E85)', 'natural gas',
       'flex-fuel (premium unleaded required/E85)',
       'flex-fuel (unleaded/natural gas)' ])

Driven_Wheels = st.sidebar.selectbox(
    "Driven Wheels" ,  
    ['rear wheel drive', 'front wheel drive', 'all wheel drive',
       'four wheel drive'])

Number_of_Doors = st.sidebar.selectbox(
    "Number of Doors" ,  
    [ 2.,  4.,  3.])


Vehicle_Size = st.sidebar.selectbox(
    "Vehicle Size" ,  
    ['Compact', 'Midsize', 'Large'])

Vehicle_Style = st.sidebar.selectbox(
    "Vehicle Style" ,  
    ['Coupe', 'Convertible', 'Sedan', 'Wagon', '4dr Hatchback',
       '2dr Hatchback', '4dr SUV', 'Passenger Minivan', 'Cargo Minivan',
       'Crew Cab Pickup', 'Regular Cab Pickup', 'Extended Cab Pickup',
       '2dr SUV', 'Cargo Van', 'Convertible SUV', 'Passenger Van'])

highway_MPG = st.sidebar.number_input(
    "highway MPG",
    min_value=1,
    value=350
)

city_mpg = st.sidebar.number_input(
    "city mpg",
    min_value=1,
    value=350
)

MSRP = st.sidebar.number_input(
    "MSRP",
    min_value=1,
    value=350
)


Market_Category = st.sidebar.number_input(
    "Market Category",
    min_value=0.5,
    max_value=15.0,
    value=4.0,
    step=0.1
)


new_data = {
    'Make': Make,
    'Model': Model,
    'Year': year,
    'Engine Fuel Type': Engine_Fuel_Type,
    'Engine HP': Engine_HP,
    'Engine Cylinders': Engine_Cylinders,
    'Transmission Type': Transmission_Type,
    'Driven_Wheels': Driven_Wheels,
    'Number of Doors': Number_of_Doors,
    'Market Category': Market_Category,
    'Vehicle Size': Vehicle_Size,
    'Vehicle Style': Vehicle_Style,
    'highway MPG': highway_MPG,
    'city mpg': city_mpg,
    'Popularity': Popularity,
    'MSRP': MSRP
           }

new_data_df = pd.DataFrame(new_data, index=[0])

## Prediction
button = st.button("Predict")
if button:
    st.write(new_data_df)
    result = pipe.predict(new_data_df)
    st.write("The predicted result is:",result[0])
