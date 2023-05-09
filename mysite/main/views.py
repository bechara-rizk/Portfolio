from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    titles=['Encryption Tools',
            'GPA Calculator',
            'Blackjack',]
    descriptions=['A collection of tools to encrypt and decrypt text, and more.',
                  'A webpage that helps students determine their overall GPA.',
                  'A webpage that allows users to play blackjack against a computer.']
    page=['/EncryptionTools',
          '/GpaCalc',
          '/blackjack',]
    github=['https://github.com/bechara-rizk/Encryption-Tools',
            'https://github.com/bechara-rizk/GPA-CALC',
            'https://github.com/bechara-rizk/blackjack',]
    images=['EncTools.svg',
            'GpaCalc.jpg',
            'blackjack.png']
    year=[2023, 2021, 2021]
    context['details']=list(zip(titles,descriptions,page,github,images,year))
    return render(request,'main/index.html', context)