// data.js

// Citations du jour
const citations = [
    "Le succès n'est pas final, l’échec n’est pas fatal : c’est le courage de continuer qui compte. – Winston Churchill 😊",
    "Croyez en vous et tout devient possible. 🌟 😄",
    "La seule façon de faire du bon travail est d’aimer ce que vous faites. – Steve Jobs 😊",
    "Chaque jour est une nouvelle chance de briller. ✨ 😎",
    "N'attendez pas l'inspiration, soyez l'inspiration. 💪 😄",
    "Le futur appartient à ceux qui croient en la beauté de leurs rêves. – Eleanor Roosevelt 🌈 😊",
    "Vous êtes plus fort que vous ne le pensez. 🔥 💪",
    "Le plus grand risque est de ne prendre aucun risque. – Mark Zuckerberg 🌟 😎",
    "Il n'y a pas de réussite sans échec. – Michael Jordan 🏆 😊",
    "Faites de votre vie un rêve, et d'un rêve, une réalité. – Antoine de Saint-Exupéry 🌠 😄",
    "Tout ce dont vous avez besoin est déjà en vous. – Rainer Maria Rilke 🌱 😊",
    "Rien n'est impossible, l'impossible prend juste un peu plus de temps. – Dan Brown ⏳ 😊",
    "L’avenir appartient à ceux qui croient à la beauté de leurs rêves. – Eleanor Roosevelt ✨ 😍",
    "Rien n’arrive jamais par hasard. – Paulo Coelho 💭 😊",
    "Visez la lune, car même si vous la manquez, vous atterrirez parmi les étoiles. – Les Brown 🌙 ✨",
    "Le succès, c’est d’aller d’échec en échec sans perdre son enthousiasme. – Winston Churchill 🌟 😊",
    "Les gagnants ne sont pas ceux qui ne tombent jamais, mais ceux qui se relèvent. 💪 😄",
    "Cessez de vous sous-estimer. Vous êtes incroyable ! ✨ 😎",
    "Le bonheur n’est pas quelque chose de prêt à l’emploi, il vient de vos propres actions. – Dalai Lama 🕊️ 😊",
    "N’arrêtez jamais d’essayer. – Albert Einstein 💡 😄",
    "Votre travail va occuper une grande partie de votre vie, et la seule manière d’être vraiment satisfait est de faire ce que vous croyez être un excellent travail. – Steve Jobs 🚀 😊",
    "Le seul endroit où le succès vient avant le travail est dans le dictionnaire. – Vidal Sassoon 📚 😄",
    "Le plus grand échec est de ne pas avoir essayé. 😟 😎",
    "Votre limite, c’est vous. – Anonyme 💪 😊",
    "Visez toujours plus haut. – Anonyme 🎯 😄",
    "Soyez vous-même, tout le monde est déjà pris. – Oscar Wilde 🤩 😊",
    "La vie commence là où commence ta zone de confort. – Neale Donald Walsch 🚀 😊",
    "On ne trouve pas l’équilibre, on le crée. – Anonyme ⚖️ 😄",
    "Faites-le aujourd’hui, parfois « demain » devient « jamais ». 💡 😎",
    "Croyez en l’impossible. – Walt Disney 🌠 😊",
    "Le succès ne consiste pas à gagner, mais à surmonter. – Vince Lombardi 🏅 😊",
    "Les seules limites qui existent sont celles que vous vous imposez. 🚀 💪",
    "Soyez le changement que vous voulez voir dans le monde. – Mahatma Gandhi 🌍 😊",
    "Rien n'est impossible. – Audrey Hepburn 💫 😄",
    "Le vrai succès, c’est d’être heureux. – Albert Schweitzer 😊 🌟",
    "La persévérance est la clé de la réussite. – Charles Dickens 🗝️ 😊",
    "Faites confiance au processus. 🛤️ 😎",
    "Les rêves ne fonctionnent que si vous travaillez dur. – John C. Maxwell 💪 🌟",
    "Ne vous contentez pas de suivre les autres, créez votre propre chemin. – Anonyme 🛤️ 😊",
    "N'ayez jamais peur de commencer. – Anonyme 🌱 💫",
    "Réalisez vos rêves avant que la vie ne passe. – Anonyme 💭 😊",
    "Le vrai courage, c’est d’avoir peur, mais de ne pas laisser la peur vous arrêter. – Anonyme 💪 😊",
    "Vos rêves ne fonctionnent que si vous travaillez dur. – Anonyme 💼 😊",
    "C'est votre moment. Saisissez-le. – Anonyme ✨ 😄",
      
];
  
  // Questions du quiz
  const questions = [
    {
      intitule: "Qui est considéré comme le père de l'informatique ?",
      choix: ["Alan Turing", "Bill Gates", "Steve Jobs", "Elon Musk"],
      bonneReponse: 0,
    },
    {
      intitule: "Que signifie l'acronyme 'WWW' ?",
      choix: [
        "World Wide Web",
        "Wide World Web",
        "Web World Wide",
        "Web With Windows",
      ],
      bonneReponse: 0,
    },
    {
      intitule: "Quel est le nom du premier moteur de recherche sur Internet ?",
      choix: ["Google", "Yahoo", "Archie", "Bing"],
      bonneReponse: 2,
    },
    {
        intitule:
          "Quelle entreprise a développé le système d’exploitation Windows ?",
        choix: ["Apple", "IBM", "Microsoft", "Google"],
        bonneReponse: 2,
      },
      {
        intitule: "Qu’est-ce qu’un virus informatique ?",
        choix: [
          "Un logiciel malveillant",
          "Un matériel défectueux",
          "Un bug dans le système",
          "Un fichier trop volumineux",
        ],
        bonneReponse: 0,
      },
      {
        intitule:
          "Quel est le navigateur web le plus utilisé dans le monde en 2024 ?",
        choix: ["Firefox", "Chrome", "Edge", "Safari"],
        bonneReponse: 1,
      },
      {
        intitule: "Que veut dire 'Cloud' en informatique ?",
        choix: [
          "Un disque dur physique",
          "Une application météo",
          "Un stockage en ligne",
          "Un type d’écran",
        ],
        bonneReponse: 2,
      },
      {
        intitule:
          "Quel appareil a popularisé l’utilisation de l’écran tactile ?",
        choix: ["Le Nokia 3310", "La Game Boy", "L’iPhone", "Le Palm Pilot"],
        bonneReponse: 2,
      },
      {
        intitule: "Qu’est-ce qu’un mot de passe fort ?",
        choix: [
          "Un mot de passe long et complexe",
          "Un mot du dictionnaire",
          "123456",
          "Le prénom de son chien",
        ],
        bonneReponse: 0,
      },
      {
        intitule: "Qui a fondé Apple avec Steve Jobs ?",
        choix: [
          "Bill Gates",
          "Steve Wozniak",
          "Elon Musk",
          "Mark Zuckerberg",
        ],
        bonneReponse: 1,
      },
      {
        intitule: "Qu’est-ce que l’intelligence artificielle (IA) ?",
        choix: [
          "Un robot tueur",
          "Une technologie imitant l’intelligence humaine",
          "Un virus informatique",
          "Un jeu vidéo",
        ],
        bonneReponse: 1,
      },
      {
        intitule: "En quelle année Google a-t-il été fondé ?",
        choix: ["1995", "1998", "2001", "2005"],
        bonneReponse: 1,
      },
      {
        intitule: "Quel est le rôle principal d’un pare-feu (firewall) ?",
        choix: [
          "Accélérer l'ordinateur",
          "Protéger contre les intrusions",
          "Augmenter la mémoire",
          "Installer des logiciels",
        ],
        bonneReponse: 1,
      },
      {
        intitule: "Quel géant du web est propriétaire de YouTube ?",
        choix: ["Apple", "Facebook", "Google", "Amazon"],
        bonneReponse: 2,
      },
      {
        intitule:
          "Quelle est la principale fonction d’un système d’exploitation ?",
        choix: [
          "Gérer les ressources matérielles",
          "Naviguer sur Internet",
          "Dessiner des images",
          "Envoyer des e-mails",
        ],
        bonneReponse: 0,
      },
      {
        intitule:
          "Lequel de ces objets n’est pas un périphérique de sortie ?",
        choix: ["Imprimante", "Écran", "Souris", "Haut-parleur"],
        bonneReponse: 2,
      },
      {
        intitule: "Quel est le principal concurrent d’Android ?",
        choix: ["Windows Phone", "iOS", "Blackberry OS", "Symbian"],
        bonneReponse: 1,
      },
      {
        intitule: "Qu’est-ce qu’un hacker éthique ?",
        choix: [
          "Un pirate qui vole des données",
          "Un expert en cybersécurité",
          "Un concepteur de jeux",
          "Un vendeur de logiciels",
        ],
        bonneReponse: 1,
      },
      {
        intitule: "Quelle unité mesure la vitesse d’un processeur ?",
        choix: ["Octets", "Watts", "Hertz", "Pixels"],
        bonneReponse: 2,
      },
      {
        intitule: "Que veut dire l’acronyme USB ?",
        choix: [
          "Universal System Base",
          "Ultra Serial Bus",
          "Universal Serial Bus",
          "Unified System Block",
        ],
        bonneReponse: 2,
      },
      {
        intitule: "Quel est l’ancêtre d’Internet ?",
        choix: ["NetLink", "WebNet", "ARPANET", "BitNet"],
        bonneReponse: 2,
      },
      {
        intitule: "Quel logiciel permet d’éditer des documents texte ?",
        choix: ["Excel", "Photoshop", "Word", "PowerPoint"],
        bonneReponse: 2,
      },
      {
        intitule:
          "Quel composant stocke les données à long terme dans un ordinateur ?",
        choix: ["RAM", "Carte graphique", "Processeur", "Disque dur"],
        bonneReponse: 3,
      },
      {
        intitule: "Quel est le métier d’un développeur web ?",
        choix: [
          "Réparer des ordinateurs",
          "Créer des sites Internet",
          "Gérer des bases de données",
          "Installer des imprimantes",
        ],
        bonneReponse: 1,
      },
      {
        intitule: "Quel est le rôle d’un antivirus ?",
        choix: [
          "Nettoyer l’écran",
          "Empêcher la surchauffe",
          "Protéger contre les logiciels malveillants",
          "Améliorer la qualité de l'image",
        ],
        bonneReponse: 2,
      },
      {
        intitule: "Combien de bits contient un octet ?",
        choix: ["4", "8", "16", "32"],
        bonneReponse: 1,
      },
      {
        intitule:
          "Comment s’appelle le langage utilisé pour interroger une base de données ?",
        choix: ["HTML", "Python", "SQL", "CSS"],
        bonneReponse: 2,
      },
      {
        intitule: "Quel réseau social appartient à Meta (ancien Facebook) ?",
        choix: ["Snapchat", "TikTok", "Instagram", "Twitter"],
        bonneReponse: 2,
      },
      {
        intitule: "Qu’est-ce qu’un cookie en informatique ?",
        choix: [
          "Un virus informatique",
          "Un fichier temporaire de navigation",
          "Un outil de programmation",
          "Une application de chat",
        ],
        bonneReponse: 1,
      },
      {
        intitule:
          "Que signifie l’icône représentant une disquette dans un logiciel ?",
        choix: ["Ouvrir", "Fermer", "Sauvegarder", "Imprimer"],
        bonneReponse: 2,
      },
    ];
  