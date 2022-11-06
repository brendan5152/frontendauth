import { Box, Card, CardContent, Grid, Typography, makeStyles } from "@material-ui/core";
import React from "react";
import Layout from "../../components/Layout";
import axios from 'axios'
import { useRouter } from 'next/router'


const useStyles = makeStyles((theme) => ({
    root: {
        marginTop: '75px',
        maxWidth: '95vw',
    },
    subtitle: {
        color: 'grey',
    },
    card: {
        cursor: 'pointer',
    }
}))

const Category = ({ category }) => {
    const classes = useStyles()
    const router = useRouter()

    const handlePartyClick = (party) => {
        router.push(`/parties/${party.slug}`)
    }

    return (
        <Layout>
            <Grid container className={classes.root}>
                <Grid item xs={12} md={3}>
                    todo filters
                </Grid>

                <Grid item xs={12} md={9}>
                    {category.party.map((party) => (
                        <Card className={classes.card} onClick={() => handlePartyClick(party)}>
                            <Box>
                                <CardContent>
                                    <Grid container>
                                        <Grid item xs={6}>
                                            <Typography variant="h5">{party.name}</Typography>
                                            <Typography variant="subtitle1" className={classes.subtitle}>{party.description}</Typography>
                                            <Typography variant="subtitle1" className={classes.subtitle}>{party.location}</Typography>
                                            <Typography variant="subtitle1" className={classes.subtitle}>{party.date}</Typography>
                                        </Grid>

                                        <Grid item xs={6}>
                                            <Typography variant="h5">{party.members.username}</Typography>
                                            <Typography variant="subtitle1">Category followers</Typography>
                                        </Grid>
                                    </Grid>
                                </CardContent>
                            </Box>
                        </Card>
                    ))}
                </Grid>
            </Grid>
        </Layout>

    )
}

export async function getServerSideProps({ query: { slug } }) {
    // Fetch data from external API
    const { data } = await axios.get(`http://127.0.0.1:8000/categories?slug=${slug}`)

    return {
        props: {
            category: data[0]
        }
    }
}


export default Category;