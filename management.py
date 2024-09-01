import argparse

def execute_command_line():
    description = 'A scrapping tool which scrapes FHIR healthcare service category and types '

    # Initiate the parser
    parser = argparse.ArgumentParser(description=description)


    # Add long and short argument
    parser.add_argument("--filepath", "-f", help="file to write results to",type=str,required=False)
    parser.add_argument("--url","-u",help='link of page to scrape',type=str,required=True)
    parser.add_argument("--format", help='format to save file. Defaults to csv', type=str, required=False)

    args = parser.parse_args()

    return args.filepath,args.url, args.format