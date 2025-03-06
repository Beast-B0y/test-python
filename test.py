def calculer_note_sur_20():
  """
  Demande la note obtenue et la note maximale, puis calcule la note sur 20.
  """
  try:
    note_obtenue = float(input("Note obtenue : "))
    note_maximale = float(input("Note maximale : "))

    note_sur_20 = (note_obtenue / note_maximale) * 20

    # Limiter la note entre 0 et 20
    note_sur_20 = max(0, min(20, note_sur_20))

    print("Note sur 20 : {:.2f}".format(note_sur_20))

  except (ValueError, ZeroDivisionError):
    print("Erreur de saisie.")

calculer_note_sur_20()