import joblib


modele_prediction = joblib.load('prediction/modele_prediction_V2.mod')

def prediction(s,nh,nc,nb,nv):
    population = nh/s
    commerce = nc/s
    transport = nb/s
    SNCF = nv/s
    # estimation = round(modele_prediction.predict([[population,commerce,transport,SNCF]])[0],3)
    estimation = round(modele_prediction.predict([[population,commerce,transport,SNCF]])[0]*100,2)


    if estimation < 20 :
        interet = "Projet d'implantation pas intéressant "
    elif estimation < 25 :
        interet = "Projet d'implantation peu intéressant "
    elif estimation < 50 :
        interet = "Projet d'implantation intéressant "
    else:
        interet = "Projet d'implantation très intéressant "


    return estimation,interet
