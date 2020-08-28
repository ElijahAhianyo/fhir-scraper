import argparse

def execute_command_line():
    description = 'A scrapping tool which scrapes FHIR healthcare service category and types '

    # Initiate the parser
    parser = argparse.ArgumentParser(description=description)


    # Add long and short argument
    parser.add_argument("--file", "-f", help="file to write results to",type=str,required=True)
    parser.add_argument("--url","-u",help='link of page to scrape',type=str,required=True)

    args = parser.parse_args()

    return args.file,args.url