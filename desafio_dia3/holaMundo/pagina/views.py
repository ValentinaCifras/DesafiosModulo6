from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""
        <body style="background-color:#000000;">
           <center> 
            <h1 style="color:#FFFFFF;">Lorem ipsum, dolor sit amet consectetur adipisicing elit</h1>
                <h3 style="color:#FFFFFF;">Lorem ipsum, dolor sit amet</h3>
            </center>
        </body>
        """
        )

def about(request):
    return HttpResponse(
        """
    <body style="background-color:#000000;">
     <center>   
    <p style="color:#FFFFFF;">Lorem ipsum dolor sit amet consectetur adipisicing elit. Eius aspernatur sunt repudiandae consequatur dicta
    necessitatibus excepturi, quae quia amet cum deleniti dolore, magni ex earum! Ea sunt est soluta repellendus.
    Ullam quod voluptatibus corrupti soluta quidem quis temporibus natus, consequatur atque impedit mollitia
    pariatur officia dolore officiis quia, dolor vero! Suscipit numquam vel explicabo? Doloremque sequi aliquid et
    minus consequatur.
    Mollitia quisquam nemo nam excepturi, eos recusandae! Expedita pariatur consequatur ut laborum perspiciatis
    voluptas eius itaque obcaecati, facilis dignissimos labore aut, iure quo aspernatur ducimus blanditiis repellat
    libero velit ipsam.</p>

    <img src="https://imageio.forbes.com/specials-images/imageserve/5f8dc21e8627c768d4342ce6/Porte-de-Soller--Palma-Mallorca/960x0.jpg?format=jpg&width=1440" height=300px>
    </center>
    </body>
        """)

def form(request):
    return HttpResponse(
        """
        <body style="background-color:#000000;">
        <center>
       <h2 style="color:#FFFFFF;">Dejanos tu nombre y correo y te contactaremos</h2>

        <form action="/action_page.php">
        <label for="nombre" style="color:#FFFFFF;">Tu nombre:</label><br>
        <input type="text" id="name"><br>
        <label for="correo" style="color:#FFFFFF;">Tu correo electronico:</label><br>
        <input type="text" id="correo"><br><br>
        <input type="submit" value="Enviar">
        </form> 


        </center>
        </body>
        """)