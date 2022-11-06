import mongoose from 'mongoose'

const eventSchema = new mongoose.Schema({
    title: String,
    Shortdescription: String,
    Longdescription: String,
    Calendersummary: String,
    TitleEN: String,
    ShortdescriptionEN: String,
    LongdescriptionEN: String,
    CalendersummaryEN: String,
    Locatienaam: String,

}, { timestamps: true })

//het zelfde
// mongoose.models = {}
let Dataset = mongoose.models.events || mongoose.model('events', eventSchema)

export default Dataset;

