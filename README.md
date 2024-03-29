<!-- Readme Start here -->

<!-- Load logo from readme/logo.jpg -->
<div align="center">
  <img src="readme/logo.jpg" width="200" alt="logo" />
</div>


<!-- Title -->
<h1 align="center" style="border: none">
Modeling RDF Data with LA Public Safety Data
</h1>


<!-- Shield IO - very nice icons -->
<div align="center">

[![Contributors][contributors_shield]][contributors_url]
[![Forks][forks_shield]][forks_url]
[![Stargazers][stars_shield]][stars_url]
[![Issues][issues_shield]][issues_url]
[![MIT License][license_shield]][license_url]
[![LinkedIn][linkedin_shield]][linkedin_url]

</div>


<!-- Description -->
A demonstration of the process of creating semantic web data with RDF and publicly available datasets provided by LA city.

## Requirements
- RDF files
  - [1000 Data]
  - [5000 Data]
  - [10000 Data]
  - [50000 Data]
  - [100000 Data]
  - [Full Data]

## Executable 
 - [Windows]


## Sample Generated RDF File
```XML
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
  xmlns:ns1="https://data.lacity.org/"
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
  <ns1:CrimeReport rdf:about="https://data.lacity.org/Report#1">
    <ns1:hasCrime>
      <ns1:Crime rdf:about="https://data.lacity.org/Crime#0">
        <ns1:hasCrimeCommitted rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">624</ns1:hasCrimeCommitted>
        <ns1:hasCrimeCommited4 rdf:datatype="http://www.w3.org/2001/XMLSchema#integer"></ns1:hasCrimeCommited4>
        <ns1:hasCrimeCommited3 rdf:datatype="http://www.w3.org/2001/XMLSchema#integer"></ns1:hasCrimeCommited3>
        <ns1:hasCrimeCrimmitedDescription rdf:datatype="http://www.w3.org/2001/XMLSchema#string">BATTERY - SIMPLE ASSAULT</ns1:hasCrimeCrimmitedDescription>
        <ns1:hasCrimeCommited1 rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">624</ns1:hasCrimeCommited1>
        <ns1:hasCrimeCommited2 rdf:datatype="http://www.w3.org/2001/XMLSchema#integer"></ns1:hasCrimeCommited2>
      </ns1:Crime>
    </ns1:hasCrime>
    <ns1:hasLocation>
      <ns1:Location rdf:about="https://data.lacity.org/Location#1">
        <ns1:hasLongitude rdf:datatype="http://www.w3.org/2001/XMLSchema#double">-118.2978</ns1:hasLongitude>
        <ns1:hasLatitude rdf:datatype="http://www.w3.org/2001/XMLSchema#double">34.0141</ns1:hasLatitude>
        <ns1:hasAddress rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1100 W  39TH                         PL</ns1:hasAddress>
        <ns1:hasAreaName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Southwest</ns1:hasAreaName>
        <ns1:hasReportingDisctrictNumber rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">377</ns1:hasReportingDisctrictNumber>
        <ns1:hasCrossStreet rdf:datatype="http://www.w3.org/2001/XMLSchema#string"></ns1:hasCrossStreet>
        <ns1:hasAreaID rdf:datatype="http://www.w3.org/2001/XMLSchema#string">03</ns1:hasAreaID>
      </ns1:Location>
    </ns1:hasLocation>
    <ns1:hasMocodes rdf:datatype="http://www.w3.org/2001/XMLSchema#string">0444 0913</ns1:hasMocodes>
    <ns1:hasPart1-2 rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</ns1:hasPart1-2>
    <ns1:hasDateReported rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-01-08</ns1:hasDateReported>
    <ns1:hasWeapon>
      <ns1:Weapon rdf:about="https://data.lacity.org/Weapon#0">
        <ns1:hasWeaponCode rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">400</ns1:hasWeaponCode>
        <ns1:hasWeaponDescription rdf:datatype="http://www.w3.org/2001/XMLSchema#string">STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE)</ns1:hasWeaponDescription>
      </ns1:Weapon>
    </ns1:hasWeapon>
    <ns1:hasPerson>
      <ns1:Person rdf:about="https://data.lacity.org/Person#1">
        <ns1:hasSex rdf:datatype="http://www.w3.org/2001/XMLSchema#string">F</ns1:hasSex>
        <ns1:hasAge rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">36</ns1:hasAge>
        <ns1:hasDescendent rdf:datatype="http://www.w3.org/2001/XMLSchema#string">B</ns1:hasDescendent>
      </ns1:Person>
    </ns1:hasPerson>
    <ns1:hasStatus>
      <ns1:Status rdf:about="https://data.lacity.org/Status#0">
        <ns1:hasStatusCode rdf:datatype="http://www.w3.org/2001/XMLSchema#string">AO</ns1:hasStatusCode>
        <ns1:hasStatusDescription rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Adult Other</ns1:hasStatusDescription>
      </ns1:Status>
    </ns1:hasStatus>
    <ns1:hasID rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">10304468</ns1:hasID>
    <ns1:hasPremise>
      <ns1:Premise rdf:about="https://data.lacity.org/Premise#0">
        <ns1:hasPremiseDescription rdf:datatype="http://www.w3.org/2001/XMLSchema#string">SINGLE FAMILY DWELLING</ns1:hasPremiseDescription>
        <ns1:hasPremiseCode rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">501</ns1:hasPremiseCode>
      </ns1:Premise>
    </ns1:hasPremise>
    <ns1:hasDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-01-08</ns1:hasDate>
    <ns1:hasTime rdf:datatype="http://www.w3.org/2001/XMLSchema#time">22:30:00</ns1:hasTime>
  </ns1:CrimeReport>
  <ns1:ArrestReport rdf:about="https://data.lacity.org/Report#0">
    <ns1:hasReporType rdf:datatype="http://www.w3.org/2001/XMLSchema#string">RFC</ns1:hasReporType>
    <ns1:hasPerson>
      <ns1:Person rdf:about="https://data.lacity.org/Person#0">
        <ns1:hasSex rdf:datatype="http://www.w3.org/2001/XMLSchema#string">M</ns1:hasSex>
        <ns1:hasAge rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">31</ns1:hasAge>
        <ns1:hasDescendent rdf:datatype="http://www.w3.org/2001/XMLSchema#string">W</ns1:hasDescendent>
      </ns1:Person>
    </ns1:hasPerson>
    <ns1:hasBooking>
      <ns1:Booking rdf:about="https://data.lacity.org/Booking#0">
        <ns1:hasBookingCode rdf:datatype="http://www.w3.org/2001/XMLSchema#integer"></ns1:hasBookingCode>
        <ns1:hasBookingLocation rdf:datatype="http://www.w3.org/2001/XMLSchema#string"></ns1:hasBookingLocation>
        <ns1:hasBookingDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date"></ns1:hasBookingDate>
        <ns1:hasBookingTime rdf:datatype="http://www.w3.org/2001/XMLSchema#time"></ns1:hasBookingTime>
      </ns1:Booking>
    </ns1:hasBooking>
    <ns1:hasLocation>
      <ns1:Location rdf:about="https://data.lacity.org/Location#0">
        <ns1:hasAreaID rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">14</ns1:hasAreaID>
        <ns1:hasLatitude rdf:datatype="http://www.w3.org/2001/XMLSchema#double">33.988</ns1:hasLatitude>
        <ns1:hasAddress rdf:datatype="http://www.w3.org/2001/XMLSchema#string">25TH</ns1:hasAddress>
        <ns1:hasReportingDistrictNumber rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1431</ns1:hasReportingDistrictNumber>
        <ns1:hasCrossStreet rdf:datatype="http://www.w3.org/2001/XMLSchema#string">OCEAN FRONT                  WK</ns1:hasCrossStreet>
        <ns1:hasLongtitude rdf:datatype="http://www.w3.org/2001/XMLSchema#double">-118.4703</ns1:hasLongtitude>
        <ns1:hasAreaName rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Pacific</ns1:hasAreaName>
      </ns1:Location>
    </ns1:hasLocation>
    <ns1:hasArrestType rdf:datatype="http://www.w3.org/2001/XMLSchema#string">I</ns1:hasArrestType>
    <ns1:hasCharge>
      <ns1:Charge rdf:about="https://data.lacity.org/Charge#0">
        <ns1:hasChargeCode rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">56.06.2(A)</ns1:hasChargeCode>
        <ns1:hasChargeGroupCode rdf:datatype="http://www.w3.org/2001/XMLSchema#integer"></ns1:hasChargeGroupCode>
        <ns1:hasChargeDescription rdf:datatype="http://www.w3.org/2001/XMLSchema#string"></ns1:hasChargeDescription>
        <ns1:hasChargeGroupDescription rdf:datatype="http://www.w3.org/2001/XMLSchema#string"></ns1:hasChargeGroupDescription>
      </ns1:Charge>
    </ns1:hasCharge>
    <ns1:hasTime rdf:datatype="http://www.w3.org/2001/XMLSchema#time">17:20:00</ns1:hasTime>
    <ns1:hasDispositionDescription rdf:datatype="http://www.w3.org/2001/XMLSchema#string">MISDEMEANOR COMPLAINT FILED</ns1:hasDispositionDescription>
    <ns1:hasID rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">201412685</ns1:hasID>
    <ns1:hasDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2020-06-10</ns1:hasDate>
  </ns1:ArrestReport>
</rdf:RDF>
```

## Datasets
 - [Arrest Data from 2020 to Present]
 - [Crime-Data-from-2020-to-Present]

## Documentation
 - [Objective]
 - [Data Mapping]
 - [RDF Relationship]
 - [Presentation]

<!-- Include your major tools and frameworks -->
## Built With
- [Python]
- [RdfLib]


<!-- Collaborators information -->
## Collaborators
- [Sotheanith Sok]
- [Lauro Cabral]
- [Christopher Vargas]

## Course
- [CECS 571 - Fundamentals of Semantic Web technologies]

<!-- License -->
## License
This project is licensed under the MIT License - see the [LICENSE.md][license_url] file for details


<!-- Shoutout to other projects, plugin, or minor tools -->
## Acknowledgments
Special thank to
- [Best-README-Template] - the readme template.


<!-- References -->
<!-- Shield Icons-->
[contributors_shield]: https://img.shields.io/github/contributors/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data.svg?style=for-the-badge
[forks_shield]: https://img.shields.io/github/forks/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data.svg?style=for-the-badge
[stars_shield]: https://img.shields.io/github/stars/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data.svg?style=for-the-badge
[issues_shield]: https://img.shields.io/github/issues/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data.svg?style=for-the-badge
[license_shield]: https://img.shields.io/github/license/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data.svg?style=for-the-badge
[linkedin_shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

<!-- Shield URLs -->
[contributors_url]: https://github.com/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data/graphs/contributors
[forks_url]: https://github.com/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data/network/members
[stars_url]: https://github.com/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data/stargazers
[issues_url]: https://github.com/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data/issues
[license_url]: https://github.com/sotheanithsok/Modeling-RDF-Data-with-LA-Public-Safety-Data/blob/master/LICENSE
[linkedin_url]: https://www.linkedin.com/in/sotheanith-sok-969ab0b3/

<!-- Other links -->
[Sotheanith Sok]: https://github.com/sotheanithsok
[Best-README-Template]: https://github.com/othneildrew/Best-README-Template

[1000 Data]: https://mega.nz/file/GqoilZ7Z#2KKcFKeFqW5XtmR8MMv9iOignMM7Ry24JkkEbUbssQs
[5000 Data]: https://mega.nz/file/TqRjBTpA#IGrluV9DsOay7TCjUBwO5DHHhNcrPfcVHj3jv-reJcs
[10000 Data]: https://mega.nz/file/224mnQxS#aLRKBrrzv-rsRC20Yf4XP9LpUPL3GxiCPFc59F6KRgc
[50000 Data]: https://mega.nz/file/jrIXBJQC#613_Bazji1NXcT7Q6RGmePdwYn2HpNc3kcAarxj76NY
[100000 Data]: https://mega.nz/file/67ohQLoT#89YEoTga8BmyVgB4SUmkvhWYH7ODBqpaUpsyK3daz70
[Full Data]: https://mega.nz/file/KjRxzBgL#wxzlmuCluKd_E9Et5oaPKKZ3FaFEhKwwCArRZfoljkk
[Windows]: exec/main.exe
[Arrest Data from 2020 to Present]: https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72
[Crime-Data-from-2020-to-Present]: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8
[Objective]: doc/Project%202.pdf
[Data Mapping]: doc/DataMapping.pdf
[RDF Relationship]: doc/Relationship.pdf
[Presentation]: doc/Presentation.pdf 
[Python]: https://www.python.org/
[RdfLib]: https://rdflib.readthedocs.io/en/stable/
[Lauro Cabral]: https://github.com/Lauro199471
[Christopher Vargas]: https://github.com/ctopher-vargas
[CECS 571 - Fundamentals of Semantic Web technologies]: http://catalog.csulb.edu/preview_course_nopop.php?catoid=5&coid=40046





