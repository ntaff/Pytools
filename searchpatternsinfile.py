# Recherche une suite de chaînes de caractères dans un fichiers, lorsque les chaînes sont situées à moins de N lignes les unes des autres
# Version fonctionnelle mais non finie

def n_lines(matches_pos, memdump):
    nblines = 20
    mini, maxi = min(matches_pos), max(matches_pos)
    return memdump[mini:maxi].count('\n') <= nblines

def print_extract_between_rec(diff, mini,maxi,memdump):
  l = []
  extract_between_recA(diff, l, mini,maxi,memdump)

def extract_between_recA(diff, l, mini,maxi,memdump):
  if (mini == maxi+diff):
    print ''.join(l)
  else :
    l.append(memdump[mini-diff])
    extract_between_recA(diff, l, mini+1,maxi,memdump)

def main ():
    diff = 20
    callslist = ['memcpy', 'RtlClearAllBits', 'NtSetInformationFile']
    try:
      file = open('example.txt', 'rb', 0)
    except IOError:
      print "Memdump file not found in current directory..."
      return 1
    memdump = file.read()
    try:
      all_matches = [memdump.index(apicall) for apicall in callslist]
    except ValueError:
      print "One or more string(s) are not present(s) in given memory dump..."
      return 1
    while True:
        if n_lines(all_matches, memdump):
            print str(min(all_matches)) + " " + str(max(all_matches))
            print_extract_between_rec(diff, min(all_matches),max(all_matches), memdump)
            return 0
        lowest_offset = min(all_matches)
        lowest = all_matches.index(lowest_offset)
        try:
            all_matches[lowest] += 1 + memdump[lowest_offset+1:].index(callslist[lowest])
        except:
            return 1

if __name__ == "__main__":
    main()
