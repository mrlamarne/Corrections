import csv
import colorama
from colorama import Fore, Style


with open('devoir_1_le_hardware(5).csv','r')as f:
  data = csv.reader(f)
  #Boucle d'analyse du csv
  int = 0;
  for row in data:
      #Conentu du  contenu
        int += 1
        noteEtudiant = 0
        #Question1
        if "1" in row[11]:
            noteEtudiant += 0.25
        if "3" in row[11]:
            noteEtudiant += 0.25
        if "4" in row[11]:
            noteEtudiant += 0.25
        if "Plusieurs processeurs" in row[11]:
            noteEtudiant += 0.25
        #Question 2
        if "2" in row[12]:
            noteEtudiant += 1

        #Question 3
        if "3" in row[13]:
            noteEtudiant += 1
        #Question 4
        if "1" in row[14]:
            noteEtudiant += 0.5
        if "500 Giga octets" in row[14]:
            noteEtudiant += 0.5
        #Question 5
        if "1" in row[15]:
            noteEtudiant += 1
        #Question 6
        if "2" in row[16]:
            noteEtudiant += 1
        #Question 7
        if "1" in row[17]:
            noteEtudiant += 1
        #Question 8
        if "2" in row[18]:
            noteEtudiant += 0.5
        #Question 9
        if("1,2,3")in row[19]:
            noteEtudiant += 1
        else:
            if "1" in row[19]:
                noteEtudiant += 0.25
            if "2" in row[19]:
                noteEtudiant += 0.25
            if "3" in row[19]:
                noteEtudiant += 0.25
        #Question 10
        if("3")in row[20]:
            noteEtudiant += 1
        #Question 11
        if("3")in row[21]:
            noteEtudiant += 0.5
        if("Facile et moins cher à installer")in row[21]:
            noteEtudiant += 0.5
        #Question 12
        if("1")in row[22]:
            noteEtudiant += 1

        #Calcul de la note
        notesur20 = noteEtudiant *20
        notesur20 /= 12

        #Affichage

        textNote = Fore.GREEN + row[10] + " " + row[9] + ":" + Fore.BLUE + str(round(notesur20)) + "     "
        print(textNote, end="")
        print(Fore.WHITE + "(" + str(noteEtudiant) + ", rapportée sur 20 : " + str(round(notesur20)) + ")")


print("nombre de copies:" + str(int))
