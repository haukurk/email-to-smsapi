__author__ = 'haukurk'

from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree


def createCMxml(customer_id, username, password, tariff, sender_name, body, msisdn):
    """
    <summary>
    Creates a XML string according to the technical requirements of the CM MT gateway for sending a simple SMS text message

    Template for CM.nl:
    <MESSAGES>
      <CUSTOMER ID="111" />
      <USER LOGIN="xxx" PASSWORD="xxxx" />
      <TARIFF>0</TARIFF>
      <MSG>
        <FROM>IT Devision</FROM>
        <BODY TYPE="TEXT">Hello!</BODY>
        <TO>003548588282</TO>
      </MSG>
    </MESSAGES>

    </summary>
    <param name="customerId">The customer's ID</param>
    <param name="username">The username</param>
    <param name="password">The password</param>
    <param name="tariff">The tariff for the SMS message</param>
    <param name="senderName">A sendername/shortcode the SMS message</param>
    <param name="body">The text to be sent</param>
    <param name="msisdn">The recipient's MSISDN</param>
    <returns>A string according to the technical requirements of the CM MT gateway, based on the provided parameters</returns>
    """

    # MESSAGES
    messagesElement = Element("MESSAGES")

    # CUSTOMER
    customerElement = SubElement(messagesElement, "CUSTOMER")
    customerElement.set("ID", str(customer_id))

    # USER
    userElement = SubElement(messagesElement, "USER")
    userElement.set("LOGIN", username)
    userElement.set("PASSWORD", password)

    # TARIFF
    tariffElement = SubElement(messagesElement, "TARIFF")
    tariffElement.text = str(tariff)

    # MSG
    msgElement = SubElement(messagesElement, "MSG")

    # FROM
    fromElement = SubElement(msgElement, "FROM")
    fromElement.text = sender_name

    # BODY
    bodyElement = SubElement(msgElement, "BODY")
    bodyElement.set("TYPE", "TEXT")
    bodyElement.text = body

    # TO
    bodyElement = SubElement(msgElement, "TO")
    bodyElement.text = msisdn

    return tostring(messagesElement)

