import Layout from '../components/Layout'
import axios from 'axios'


/** 
 * ! This component is depreceted.
const useStyles = makeStyles((theme) => ({
  root: {
    margin: '25px auto',
    maxWidth: '95vw',
  }
}))
**/

export default function Home({ categories }) {
  //const classes = useStyles()
  return (
    <Layout>
      <Grid container className={classes.root} spacing={3}>
        {categories.map((category) => (
          <Grid item xs={12} md={4}>
          <Card>
            <CardHeader
              avatar={
                <Avatar aria-label='category'>
                  C
                </Avatar>
              }
              title={`Name: ${category.name}`}
              subheader={'Parties: ' + category.party}
            />
          </Card>
        </Grid>
        ))}
      </Grid>
    </Layout>

  )
}

export async function getServerSideProps() {
  // Fetch data from external API
  const { data } = await axios.get('http://127.0.0.1:8000/categories/')

  return {
    props: {
      categories: data
  }
}
}