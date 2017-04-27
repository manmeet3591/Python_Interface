def myround(x, prec=2, base=.05):
  return round(base * round(float(x)/base),prec)
