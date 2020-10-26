export default class Card {
    constructor(name, education, contact) {
        this.name = name;
        this.education = education;
        this.contact = contact;
        this.status = "Applied";
        this.rate = 0;
        this.rateNumber = 0;
        this.curRate = 0;
    }

    renderCard() {
        return (
            "<h5>" + this.name + "</h5>" +
            "<p>" + this.contact + "</br>" +
            this.education + "</br>" +
            "Average Rate: " + this.rate + "</p>"
        )
    }

}