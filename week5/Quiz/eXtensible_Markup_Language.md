> I've provided all possible questions, mark the ones that appear

#### Q1. What is the name of the Python 2.x library to parse XML data?

Ans: xml.etree.ElementTree

#### Q2. Which of the following are not commonly used serialization formats?

Ans :
* Dictionaries
* HTTP
* TCP

#### Q3. In this XML, which are the "simple elements"?

    <people>
        <person>
        <name>Chuck</name>
        <phone>303 4456</phone>
        </person>
        <person>
        <name>Noah</name>
        <phone>622 7421</phone>
        </person>
    </people>

Ans:
* name
* phone

> complex elements will be the rest of the options.

#### Q4. In the following XML, which are attributes?

    <person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
    </person>

Ans:
* type
* hide

#### Q5. In the following XML, which node is the parent node of node e

    <a>
    <b>X</b>
    <c>
        <d>Y</d>
        <e>Z</e>
    </c>
    </a>

Ans: c

#### Q6. Looking at the following XML, what text value would we find at path "/a/c/e"

    <a>
    <b>X</b>
    <c>
        <d>Y</d>
        <e>Z</e>
    </c>
    </a>

Ans: Z

#### Q7. What is the purpose of XML Schema?

Ans: To establish a contract as to what is valid XML

#### Q8. For this XML Schema:

    <xs:complexType name=”person”>
    <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
    </xs:sequence>
    </xs:complexType>

#### And this XML,

    <person>
    <lastname>Severance</lastname>
    <Age>17</Age>
    <dateborn>2001-04-17</dateborn>
    </person>

#### Which tag is incorrect?

Ans: Age

#### Q9. What is a good time zone to use when computers are exchanging data over APIs?

Ans: Universal Time / GMT

#### Q10. Which of the following dates is in ISO8601 format?

Ans: 2002-05-30T09:30:10Z