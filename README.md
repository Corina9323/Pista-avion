# Pista-avion
Am creat acest proiect in parteneriat cu Horjea Ana Maria. Acesta se numeste Pista unui avion si cuprinde uramtoarele elemente:
     -4 piste pt avioane;
     -2 tablouri care reprizinta plecarile si sosirile;
     -un orar cu plecari si sosiri;
     -o planificare a destinatiilor dus-intors.

Pe baza acestor elemente am construit urmatoarele programe respectiv subprograme :  
          Simulator 1  si Simulator 2
   				Avion
				  Radar
				  Main-ul.
				  Pistele sunt atriubuite  cu 0 pentru Aterizari si 1 pentru Decolari.
				  !!!!!Atentie! Aterizarile au prioritate. Daca pe pista exista un avion care vrea decoleze , mai intai va trebui sa astepte un interval de timp pentru a putea decola deoaarece prioritar este aterziarea.
	  Intervalul pentru fiecare operatiune este de 5 minute. Intre o aterizare si o decolare trebuie sa fie o diferenta de 5 minute si vom avea calcula ca distanta dintre 2 operatiuni sa fie >= cu 5 minute.
	  Ca abordarea problemei sa fie cat mai simpla am solutionat problema in felul urmator:
	   -ne-am ales un manager pentru decolari si unul pentru aterizari;
	   -vom crea 2 theread-uri prioritare;
	   -pe masusra ce ceasul va arata ora 00:00, vom verifica lista. Insa pe aceasta lista putem avea la un inv=terval de timp fie 2 aterizari si  decololare , fie 5 decolari si 0 aterizari.
	  La un moment dat, lista va fi vida deoarece nu vor exista aterizari si nici decolari.
	  Iar apoi , vom informa avionul de fiecare data cand poate decola sau ateriza.
	
	In final vom afisa  folosind cele 2 tablouri , toate cursele , companiile aeriene, ora si modul in care se vor efectua operatiunile.
				  
				
				  
				


