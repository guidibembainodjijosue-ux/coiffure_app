from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Une liste temporaire pour stocker les rendez-vous (en attendant d'utiliser une vraie base de données)
rendez_vous_db = []

@app.get("/", response_class=HTMLResponse)
def afficher_formulaire():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Réservation - Salon de Coiffure</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 50px; }
            .container { max-width: 500px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
            h2 { color: #333; }
            label { display: block; margin-top: 15px; font-weight: bold; }
            input, select { width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 4px; }
            button { background-color: #28a745; color: white; padding: 12px; border: none; width: 100%; margin-top: 20px; border-radius: 4px; font-size: 16px; cursor: pointer; }
            button:hover { background-color: #218838; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Prendre un Rendez-vous</h2>
            <form action="/reserver" method="post">
                <label for="nom">Votre Nom :</label>
                <input type="text" id="nom" name="nom" required>

                <label for="service">Type de Coiffure :</label>
                <select id="service" name="service">
                    <option value="Coupe Homme">Coupe Homme</option>
                    <option value="Coupe Femme & Brushing">Coupe Femme & Brushing</option>
                    <option value="Tresses / Coiffure Afro">Tresses / Coiffure Afro</option>
                    <option value="Coloration / Soin">Coloration / Soin</option>
                </select>

                <label for="date">Date et Heure :</label>
                <input type="datetime-local" id="date" name="date" required>

                <button type="submit">Confirmer le rendez-vous</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/reserver", response_class=HTMLResponse)
def traiter_reservation(nom: str = Form(...), service: str = Form(...), date: str = Form(...)):
    # On enregistre le rendez-vous dans notre liste
    rdv = {"nom": nom, "service": service, "date": date}
    rendez_vous_db.append(rdv)
    
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Confirmation</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 50px; text-align: center; }}
            .container {{ max-width: 500px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); margin: auto; }}
            h2 {{ color: #28a745; }}
            a {{ display: inline-block; margin-top: 20px; text-decoration: none; color: #007bff; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Félicitations {nom} !</h2>
            <p>Votre rendez-vous pour <strong>{service}</strong> le <strong>{date}</strong> a bien été enregistré.</p>
            <p>Le salon vous attend !</p>
            <a href="/">Retour à l'accueil</a>
        </div>
    </body>
    </html>
    """

@app.get("/rendez-vous")
def voir_rendez_vous():
    return {"total": len(rendez_vous_db), "liste": rendez_vous_db}
