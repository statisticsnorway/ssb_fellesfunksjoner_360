# AUTOGENERATED! DO NOT EDIT! File to edit: 03_sporre.ipynb (unless otherwise specified).

__all__ = ['avled_tverrvar']

# Cell
import pandas as pd

# Cell
def avled_tverrvar(codeprefix: str,
                   coderange:  int,
                   lettercodes: dict,
                   df: pd.DataFrame()
                  ) -> pd.DataFrame:

    """
    Denne funksjonen genererer sjekker en bred range av kode-kolonner, og slår disse sammen til en oppsummeringskolonne.\n
    Forutsetningen er at det er lignende svaralternativer på ulike spørsmål som man skal gå gjennom.\n
    F.eks. 17 spørsmål om fjernsynskanaler, hvor man spør etter 21 ulike programtyper. Og man ønsker å svare på: 'Så denne personen på denne typen program i det hele tatt?'\n


    Parameters
    ----------
    first : string\n
        Første parameter er en string som er prefikset til kolonnene, feks. 'fje10_'
    second : integer\n
        Andre parameter er ett tall som sier hvor mange kolonner som er nummerert.
        Om du sender 17 så vil den ta alle tallene som er 1-17 og da lage kolonneheadere som 'fje10_17x'
    third : dict\n
        Det tredje parameteret skal være en dict, som forteller om hvilket svaralternativ skal bli til hvilken nye kolonne.
        feks. 'a' : 'tvsport', hvor svaralternativ 'a' på alle kanaler, skal bli 'eller'-t til en avledet variabelkolonne 'tvsport'
    fourt : Pandas Dataframe\n
        Det fjerde parameteret skal være dataframen som vi opererer på.

    Returns
    -------
    DataFrame
        Returnerer dataframen som kom inn, med ny avledet kolonne.

    Raises
    ------
    ValueError\n
        Om noen av variablene inn ikke stemmer med forventede typer.
    KeyError\n
        Om noen av kolonnene det letes i, ikke finnes.
    """

    # Typechecking
    if not isinstance(codeprefix, str):
        raise ValueError('Første variabel må være en string som er prefikset til koden, feks "fje10_"')
    if not isinstance(coderange, int):
        raise ValueError('Andre variabel må være en integer som sier hvor langt kodene går fra 1, feks. 1-17 så skal den være 17.')
    if not isinstance(lettercodes, dict):
        raise ValueError('Tredje variabel må være en dictionary som linker bokstaver til kolonne-header-variabler. Feks. {"a" : "tvsport"} osv.')
    if not isinstance(df, pd.DataFrame):
        raise ValueError('Fjerde variabel må være hoveddataframen som skal opereres på.')
    # Om dataframen er tom, så er det jo ikke vits å gjøre noe
    if not len(df):
        raise ValueError('Dataframen i fjerde varabel er tom, da er det jo ikke noe poeng å gjøre dette...')


    # Loop gjennom dictionary av koder -> variabel
    for key, item in lettercodes.items():
        # Lag en tom liste
        check = []
        # For hver av nummerene i rangen
        for i in range(1, coderange+1):
            # Legg til en kode formatert med range-nummer og bokstavnøkkel i listen vi initierte over
            check.append(f'{codeprefix}{i}{key}')

        # Sjekk om alle kolonnene vi skal se i faktisk er i dataframen
        for x in check:
            if not x in df.columns:
                raise KeyError(f'Finner ikke kolonnen {x} i dataframe.')

        # Potensiell kode for å sjekke noen av kolonnene inneholder True,
        # om de gjør det, sett ny kolonne samme som "item" (tvsport feks) til True
        df.loc[df[check].any(), item] = True

        # Print hele listen vi har appendet til
        #print(check)
        # Print koden vi skal skrive til basert på logikk (kommer senere)
        #print(item)
        # Print skille mellom koder
        #print('-' * 50)

    # Test at alle kolonnene i dict-items er nå i dataframen?


    return df