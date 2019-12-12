__doc__='''
Domande per il questionario:
 - scaled_questions sono valutate su una scala da 5 (Molto) a 1 (Per nulla)
 - binary_questions sono valutate su una scale Yes/No
 - Ogni domanda va formulata in due parti, e.g.: 
 		'domanda_sul_gradimento' : 'ti &egrave; piaciuto il nostro libro?'
	 La prima parte e' il nome che avra' la colonna delle risposte nel file dei risultati, la seconda quello che viene mostrato a chi compila il questionario
'''

# Domande a risposta multipla su scale 5-1
scaled_questions={
	'q1': 'Leggere e guardare il cellulare del partner &egrave; una dimostrazione di interesse per l’altro.',
	'q2': 'Condividere con il partner le password di Facebook/Instagram dimostra che non si ha nulla da nascondere.',
	'q3': 'Ci sta che tu chieda al partner di vestirsi come piace a te.',
	'q4': '&Egrave; giusto rinunciare ad uscire con i tuoi amici se d&agrave; fastidio al tuo partner.',
	'q5': 'Condividere con altri foto intime scambiate con il partner &egrave; un modo per dimostrare quanto stiamo bene insieme.',
	'q6': 'Quando c’&egrave; qualcosa che ti fa soffrire nella relazione con il partner &egrave; utile parlarne con una persona di tua fiducia.',
}

# Domande a risposta si'/no
binary_questions={
	'q7': 'Sai cos’&egrave; il “Ciclo della violenza”?',
	'q8': 'Sai cos’&egrave; il Consultorio ?'
}


# Template HTML per il questionario
scaled_question_template='''
	<div id="content">
		<h3>${title}</h3>
		<div class="quest">
		<label>Molto</label><br><input type="radio" name="${id}" value="5">
		</div>
		<div class="quest">
		<label>Abbastanza</label><br><input type="radio" name="${id}" value="4">
		</div>
		<div class="quest">
		<label>Cos&igrave; cos&igrave;</label><br><input type="radio" name="${id}" value="3" checked>
		</div>
		<div class="quest">
		<label>Poco</label><br><input type="radio" name="${id}" value="2">
		</div>
		<div class="quest">
		<label>Per nulla</label><br><input type="radio" name="${id}" value="1">
		</div>
	</div>
'''

binary_question_template='''
	<div id="content">
		<h3>${title}</h3>
		<input type="radio" name="${id}" value="Y">S&igrave;
		<input type="radio" name="${id}" value="N">No
	</div>
'''

