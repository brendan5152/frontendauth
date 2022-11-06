import NextAuth from "next-auth"


import CredentialsProvider from "next-auth/providers/credentials";

import { MongoDBAdapter } from "@next-auth/mongodb-adapter"
import clientPromise from "./lib/mongodb";
import connectDB from "./lib/connectDB";
import Users from '../../../models/userModel';
import bcrypt from 'bcrypt';
connectDB();
export default NextAuth({
    // Configure one or more authentication providers
    // adapter: MongoDBAdapter(clientPromise),

    providers: [
        CredentialsProvider({
            // The name to display on the sign in form (e.g. "Sign in with...")
            name: "Credentials",

            credentials: {
                username: { label: "Username", type: "text", placeholder: "jsmith" },
                password: { label: "Password", type: "password" }
            },
            async authorize(credentials, req) {
                const email = credentials.email;
                const password = credentials.password;
                const user = await Users.findOne({ email })
                if (!user) {
                    throw new Error("You haven't registered yet")
                }
                if (user) {
                    return signInUser({ password, user })
                }
            }
        }),
    ],
    pages: {
        signIn: "/signin"
    },
    secret: "secret",
    database: process.env.MONGODB_URI,

})

const signInUser = async ({ password, user }) => {
    if (!user.password) {
        throw new Error("Please enter password")
    }
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
        throw new Error("Password not correct")
    }
    return user
}