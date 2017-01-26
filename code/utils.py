import sys, csv, time

def parse_csv_data(file, parse, clean, limit=float('inf')):
    print()
    start = time.time()
    with open(file) as f:
        a = []
        i= 0
        for row in csv.DictReader(f, skipinitialspace=True):
            x = clean(row.items())
            if len(a) < limit:
                if x is not None:
                    a.append({k : parse(k, v) for k, v in x})
                    i += 1
                    sys.stdout.write("\rCurrent iteration: %d." % i)
                    sys.stdout.flush()
            else:
                break
        print('\n')
        print("Processing complete. Took " + str(time.time() - start) + " seconds.\n")
        return a

def base_parse(k, v):
    try:
        return int(v)
    except Exception as e:
        try:
            return float(v)
        except Exception as e:
            return v

def print_dict(d):
    for k, v in sorted(d.items()):
        print(str(k) + " : " + str(v) + " (Type = " + type(v).__name__ + ")")
    print()


