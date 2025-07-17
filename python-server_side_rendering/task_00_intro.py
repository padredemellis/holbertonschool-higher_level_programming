#!/usr/bin/python
import os
import logging
from string import Template

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def generate_invitations(template, attendees):
    """
    Genera archivos de invitación personalizados a partir de una plantilla
    y una lista de asistentes, manejando varios casos de error.

    Args:
        template (str): La cadena de la plantilla con marcadores de posición.
        attendees (list): Una lista de diccionarios, donde cada diccionario
                          representa los datos de un asistente.
    """
    if not isinstance(template, str):
        logging.error("Invalid Input Type: Template must be a string.")
        return
    if not isinstance(attendees, list):
        logging.error("Invalid Input Type: Attendees must be a list of dictionaries.")
        return
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            logging.error(f"Invalid Input Type: Attendee at index {i} is not a dictionary.")
            return

    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee_data in enumerate(attendees):
        processed_data = attendee_data.copy()

        for placeholder in placeholders:
            if placeholder not in processed_data or processed_data[placeholder] is None:
                processed_data[placeholder] = "N/A"

        try:
            invitation_template = Template(template)
            personalized_invitation = invitation_template.safe_substitute(processed_data)

            output_filename = f"output_{i + 1}.txt"
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(personalized_invitation)
            logging.info(f"Generated {output_filename}")

        except Exception as e:
            logging.error(f"Error processing invitation for attendee {i + 1}: {e}")
            continue
