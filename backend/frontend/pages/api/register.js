import bcrypt from 'bcrypt';
import Users from '../../models/userModel';

export default async function handler(req, res) {
    const body = req.body
    console.log(body)
    const userExist = await Users.findOne({ email: body.email });
    if (userExist) {
        res.status(200).json({ message: 'Already registered' })
        return;
    }


    // generate salt to hash password
    // const salt = await bcrypt.genSalt(10);
    // // now we set user password to hashed password
    // const hashpass = await bcrypt.hash(body.password, salt);
    // const user = new Users({ email: body.email, password: hashpass });
    // await user.save()
    const hashPass = await bcrypt.hash(body.password, 12)
    const newUser = new Users({ email: body.email, password: hashPass })
    await newUser.save()

    res.status(200).json({ message: 'Registered successfully' })


}
