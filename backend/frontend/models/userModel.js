import mongoose from 'mongoose'

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        default: 'user'
    },
    email: {
        type: String
    },
    password: {
        type: String
    },
    image: {
        type: String,
        default: 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwaterfordwhispersnews.com%2Fwp-content%2Fuploads%2F2017%2F05%2Fmaxresdefault.jpg&f=1&nofb=1&ipt=a9786cc05e75a6e142652947f0489713d8fd27a2bff27ec364fa25d485be0a4a&ipo=images'
    },

}, { timestamps: true })

let Dataset = mongoose.models.users || mongoose.model('users', userSchema)
export default Dataset;