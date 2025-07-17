def generate_invitations(template, attendees):
    # Verificar tipos de entrada
    if not isinstance(template, str):
        print("Error: Invalid input types. 'template' must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Invalid input types. 'attendees' must be a list of dictionaries.")
        return
    
    # Verificar plantilla vacía
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Verificar lista vacía
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Procesar cada asistente
    for idx, attendee in enumerate(attendees, start=1):
        # Crear copia de la plantilla para modificar
        invitation = template
        
        # Reemplazar cada placeholder o usar "N/A" si falta
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            placeholder = f"{{{key}}}"
            invitation = invitation.replace(placeholder, str(value) if value is not None else "N/A")
        
        # Escribir archivo de salida
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
        except IOError as e:
            print(f"Error writing file {filename}: {e}")