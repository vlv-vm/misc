select * from Drzava
--U tablicu Drzava dodajte jedan novi stupac naziva BrojStanovnika koji ima sve vrijednosti NULL.
ALTER TABLE Drzava ADD BrojStanovnika NVARCHAR(50)

--Kreirajte pogled vwDrzava koji dohvaca prvih 5 država s najvecim brojem kupaca. Potrebno je prikazati
--stupce Naziv države, Broj stanovnika i Broj kupaca. Ukoliko nije unesena vrijednost za BrojStanovnika
--potrebno je ispisati 0 (nula). Pomocu CASE naredbe u trecem stupcu naziva Opis dodati sljedecu kategorizaciju:
-- [0;3000> -> Mali broj kupaca
-- [3000,6000> -> Srednji broj kupaca
-- >=6000 -> Veliki broj kupaca
--Pogled mora biti zašti´cen enkripcijom, a s tablicama na koje se referencira mora biti uspostavljena cvrsta veza.

CREATE VIEW vwDrzava
WITH ENCRYPTION, SCHEMABINDING
AS
SELECT TOP 5 Drzava.Naziv, ISNULL(Drzava.BrojStanovnika, 0) AS 'Broj Stanovnika', count(IDKupac) AS 'BrojKupaca', 
CASE
WHEN COUNT(IDKupac) >= 0 AND COUNT(IDKupac) < 3000 THEN 'Mali broj kupaca'
WHEN COUNT(IDKupac) >= 3000 AND COUNT(IDKupac) < 6000 THEN 'Srednji broj kupaca'
WHEN COUNT(IDKupac) >= 6000 THEN 'Veliki broj kupaca'
END AS 'Opis'
FROM dbo.Drzava
LEFT JOIN dbo.Grad ON IDDrzava=DrzavaID
LEFT JOIN dbo.Kupac ON IDGrad=GradID
GROUP BY Drzava.Naziv, ISNULL(Drzava.BrojStanovnika,0)
ORDER BY COUNT(IDKupac) DESC

select * from vwDrzava
DROP VIEW vwDrzava

ALTER TABLE Drzava
DROP COLUMN BrojStanovnika

--------------------------
Kreirajte pogled vwProizvodi koji dohvaca ID, naziv, broj proizvoda, boju i cijenu bez PDV-a prvih 50 %
najjeftinijih proizvoda koji zadovoljavaju sve sljedece uvjete:
 Bilo koja od boja Crna, Srebrna, Crvena, Žuta
 Cijena bez PDV-a nije unutar intervala [600;800]
 Naziv proizvoda ne sadrži niti jednu znamenku
 Nakon treceg znaka broj proizvoda ne smije sadržavati samo brojeve, npr. CA-5965 je potrebno
izbaciti, a u obzir dolazi GL-H102-M (jer ima i slove i brojeve).
Stupac broj proizvoda preimenujte u Šifra, a cijenu bez PDV-a u Cijena.

Preko pogleda vwProizvodi u tablicu proizvoda dodajte novi proizvod, ali tako da unesete sve vrijednosti.
--------------------------

CREATE VIEW vwProizvodi
AS
SELECT TOP 50 PERCENT IDProizvod, Naziv, BrojProizvoda AS 'Šifra', Boja, CijenaBezPDV as 'Cijena' FROM Proizvod
WHERE (Boja IN ('Crna', 'Srebrna', 'Crvena', 'Žuta')) AND (CijenaBezPDV NOT BETWEEN 600 AND 800) AND (Naziv NOT LIKE '%[0-9]%') AND (BrojProizvoda NOT LIKE '___%[0-9]')
ORDER BY Cijena ASC

INSERT INTO vwProizvodi VALUES('TestNaziv', 'TestSifra', 'Crvena', '0.00')

---------------------
Promijenite pogled da onemogucite unos novih podataka u tablicu. 
---------------------

ALTER VIEW vwProizvodi
AS
SELECT TOP 50 PERCENT IDProizvod,Naziv,BrojProizvoda AS 'Šifra',Boja,CijenaBezPDV AS 'Cijena' FROM dbo.Proizvod
WHERE (Boja IN ('Crna','Srebrna','Crvena','Žuta')) AND (CijenaBezPDV NOT BETWEEN 600 AND 800) AND (Naziv NOT LIKE '%[0-9]%') AND (BrojProizvoda NOT LIKE '___%[0-9]')
ORDER BY Cijena ASC
WITH CHECK OPTION


---------------------
Kreirajte pogled vwKK, zašticen enkripcijom i cvrstom vezom prema referenciranim tablicama,
koji za pojedinu kreditnu karticu dohva´ca ukupan pla´ceni iznos svih raˇcuna koji pripadaju kreditnoj kartici.
Stupac je potrebno nazvati Ukupan pla´ceni iznos, te je dodatno potrebno prikazati stupce ID, Tip i Broj
kartice. One kartice s kojima još nije ništa pla´ceno trebaju imati vrijednost 0. Potrebno je dohvatiti
prvih 99% kartica koji imaju najmanji Ukupan pla´ceni iznos, pri ˇcemu se uzimaju u obzir samo one kartice
--koje imaju vrijednost Ukupan pla´ceni iznos unutar intervala [0;1000>.

Dohvatite one kreditne kartice kroz pogled vwKK koje su tipa Diners ili Visa, i koje u Broj-u
kreditne kartice bilo gdje imaju znakovni niz 666. Poredajte dohvat od najve´ce do najmanje vrijednosti
Ukupan pla´ceni iznos.
---------------------

create view vwKK
with encryption, schemabinding
as
select top 99 percent IDKreditnaKartica,Tip,Broj,ISNULL(SUM(UkupnaCijena),0) as 'Ukupni placeni iznos' from dbo.KreditnaKartica
LEFT JOIN dbo.Racun on KreditnaKarticaID=IDKreditnaKartica
LEFT JOIN dbo.Stavka on IDRacun=RacunID
GROUP BY IDKreditnaKartica,Tip,Broj
HAVING ISNULL(SUM(UkupnaCijena),0)>=0 and ISNULL(SUM(UkupnaCijena),0)<1000
ORDER BY ISNULL(SUM(UkupnaCijena),0) ASC


