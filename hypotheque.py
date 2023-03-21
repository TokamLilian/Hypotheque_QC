#Nom: Ange Lilian TCHOMTCHOUA TOKAM

#le programme hypotheque.py calcule le montant du versement mensuel
#pour rembourser un prêt hypothécaire de l'utilisateur et affiche une
#grille des différents montant au fil du contrat 

nomb_versement = 12 

def total_versements (nombre_annees):                                                  #calcule le nombre de versements de tout le contrat
    total_de_versements = nomb_versement * nombre_annees
    return total_de_versements


def interet (taux_hypothecaire): 
    taux_hypothecaire = taux_hypothecaire / 100                                        #convertir le pourcentage du taux en decimal

    interet_mensuel = taux_hypothecaire / nomb_versement                               #calcule l'intérêt sur le montant pour chaque mois
    interet_mensuel = round((interet_mensuel), 4)                                      #arrondir l'intérêt mensuel à decimales
    return interet_mensuel


def total_interet (total_de_versements, interet_mensuel):                              #calcule le taux mensuel total 
    interet_total = (1 + interet_mensuel) ** -(total_de_versements)
    interet_total = round(interet_total, 4)
    return interet_total


def versement(montant_pret, interet_mensuel, interet_total):                           #calcule le montant à versé pour le mois

    montant = montant_pret * interet_mensuel                                           #le montant du prêt avec les interets appliqués 
    versement_mensuel = montant / (1 - interet_total)                                  #on divise par 1 - (l'intérêt total)
    versement_mensuel = round(versement_mensuel, 4)

    return versement_mensuel


def montant(montant_pret, capital):        
    montant_pret = montant_pret - capital                                              #le nouveau montant restant est le montant payé sans 
    montant_pret = round(montant_pret, 4)                                              #intérêt deduit du montant preté 
    return montant_pret            
     
             
def calcul_capital(versement_mensuel, interet_paye):                   
    capital = versement_mensuel - interet_paye                                         #on calcule le capital qui est le montant payé  
    capital = round(capital, 4)                                                        #hors intérêt                                     
    return capital 


def hypotheque(montant_pret, taux_hypothecaire, nombre_annees):                        #cette fonction etablie tout les principaux calculs de l'hypotheque
                                                                                       
    total_de_versements = total_versements(nombre_annees)
        
    interet_mensuel = interet(taux_hypothecaire)                                

    interet_total = total_interet(total_de_versements, interet_mensuel)

    versement_mensuel = versement(montant_pret, interet_mensuel, interet_total)

    print("Balance",montant_pret,"$")                                                  #imprimme le montant initial preté 
    print(" ")         
           
    i = 1          
           
    while montant_pret > 0:                                                            #on verifie si le montant total payé a atteint 
                                                                                       #le montant initialement preté
           
        interet_paye = montant_pret * interet_mensuel                                  #calcul l'intérêt à payer sur le montant du mois en cours
        interet_paye = round(interet_paye, 4)          
                           
               
           
        if montant_pret < versement_mensuel:                                           #on ne doit pas payer plus que ce qui reste, donc
            versement_mensuel = montant_pret + interet_paye                            #le dernier versement mensuel devient le montant restant 
            versement_mensuel = round(versement_mensuel, 4)                            #et l'intérêt restant à payer
                               
            capital=montant_pret                                                       #le nouveau capital à payer est le montant restant                                          
            montant_pret = montant(montant_pret, capital)

        else: 
            capital=calcul_capital(versement_mensuel, interet_paye)
                    
            montant_pret = montant(montant_pret, capital)

        print ('Mois', i)

        print ('Versement mensuel', versement_mensuel,"$")
        print ('intérêt payé', interet_paye,"$")
        print ('Montant payé', capital,"$")  
        print ('Balance',montant_pret,"$")
        print(" ")

        i += 1     

    print("Fin du calcul") 


def verification(montant_pret, taux_hypothecaire, nombre_annees):
    while montant_pret < 0 or nombre_annees <= 0 or taux_hypothecaire < 0:             #on test si aucune valeur n'est negative

        print('Veuillez entrer des valeurs supérieures à zéro(0)')                     #on modifira par la suite, uniquement les vraibles qui sont négatives
        if montant_pret <= 0: 
            montant_pret = int(input('Entrer le montant du prêt: '))
        elif taux_hypothecaire <= 0:
            taux_hypothecaire = float(input('Entrer le taux hypothécaire en decimal: '))
        elif nombre_annees <= 0:
            nombre_annees = int(input('Entrer la durée du prêt en années: '))

    while taux_hypothecaire >= 100:                                                   #on veut un taux hypothécaire d'au plus 100% 
        print('Mauvaise valeur du taux hypothécaire')
        taux_hypothecaire = float(input('Entrer un taux hypothécaire en decimal inférieur à 100: '))                                                          
     
    hypotheque (montant_pret, taux_hypothecaire, nombre_annees) 


#pour l'entrée manuelle des valeurs par l'utilisateur
montant_pret = int(input('Entrer le montant du prêt: '))
taux_hypothecaire = float(input('Entrer le taux hypothécaire en decimal: '))
nombre_annees = int(input('Entrer la durée du prêt en années: '))

verification(montant_pret, taux_hypothecaire, nombre_annees)