import { Box, Card, CardContent, Grid, Typography, makeStyles, List, ListItem, ListItemText, Button} from "@material-ui/core";
import React from "react";
import Layout from "../../components/Layout";
import axios from 'axios'
import GetServerSideProps from "./index.js";



const useStyles = makeStyles((theme) => ({
    root: {
        marginTop: '75px',
        maxWidth: '95vw'
    },
    buyTicket: {
        marginTop: '15px'
    },
    description: {
        paddingTop: '15px'
    }
}))



function EventPage({ event }) {
    const classes = useStyles()
    return (
        <Layout>
            <h1>{event.description }</h1>
        </Layout>
    )
}

// Called at build time
export async function getStaticPaths() {
    // Call to the api end point to get all parties
    const res = await fetch(`http://localhost:8000/parties/`)
    const events = await res.json()

    // Get the paths we want to pre-render based on parties
    const paths = events.map((event) => ({
        params: { slug: event.slug },
    }))

    // Only pre-render needed otherwise 404 page shows.
    return {
        paths,
        fallback: false
    }
    
}

// Called at build time
export async function getStaticProps({ params }) {
    // Params contains the party `slug`.
    // If the route is like /parties/1, then params.slug is 1
    const res = await fetch(`http://localhost:8000/parties/${params.slug}`)
    const event = await res.json()

    console.log(params)
    console.log(event)
    // Pass post data to the page via props
    return { props: { event } }
}


export default EventPage