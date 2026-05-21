#!/usr/bin/python3

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template
    and a list of attendee dictionaries.
    """

    # Check template type
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    # Check attendees type
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return

    # Check if every item in attendees is a dictionary
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendees must be a list of dictionaries")
            return

    # Check empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):

        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # Replace placeholders
        invitation = template
        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))

        # Create output file
        filename = f"output_{index}.txt"

        try:
            with open(filename, "w") as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
