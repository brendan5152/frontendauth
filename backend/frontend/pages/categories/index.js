import { Box, Card, CardContent, Grid, Typography, makeStyles } from "@material-ui/core";
import React from "react";
import Layout from "../../components/Layout";

const Id = () => {
    return (
        <Layout>
            <Grid container>
                <Grid item xs={12} md={3}>
                    todo filters
                </Grid>
                <Grid item xs={12} md={9}>
                    <Card>
                        <Box>
                            <CardContent>
                                <Grid container>
                                    <Grid item xs={6}>
                                        <Typography variant="h5">Name</Typography>
                                        <Typography variant="subtitle1">Description</Typography>
                                        <Typography variant="subtitle1">Party Location</Typography>
                                        <Typography variant="subtitle1">Party Owner</Typography>
                                    </Grid>

                                    <Grid item xs={6}>
                                        <Typography variant="h5">Active members</Typography>
                                        <Typography variant="subtitle1">Party time</Typography>
                                    </Grid>
                                </Grid>
                            </CardContent>
                        </Box>
                    </Card>
                </Grid>
            </Grid>
        </Layout>

    )
}

export default Id;