import { Divider } from "@material-ui/core"
import { Class } from "@material-ui/icons"
import { useSession, signIn, signOut } from "next-auth/react"

import Layout from "../components/Layout"
import EventCard from "./eventCard"


export async function getStaticProps() {
  // Call an external API endpoint to get posts
  const res = await fetch('https://open.data.amsterdam.nl/Festivals.json')
  const events = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      events,
    },
  }
}

// {events.map((event) => (
//   <li>{event.title}</li>
// ))}

function Events({events}) {
  // ! This is the session object
  // const { data: session } = useSession({
  //     required: true
  // })
  return (
      <Layout>
          <div className='py-6 my-4 max-w-sm shadow-xl border-slate-100 border-2 text-center rounded-3xl'>
          <h1 className='text-2xl font-normal'>Upcomming Events</h1>
          </div>
          
          <ul role="list" className="grid grid-cols-1 gap-6 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 ">
              {events.map((event) => (
              <div class="flex justify-center">
                 <div class="rounded-lg shadow-lg bg-white max-w-sm transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 duration-300">
                   <a href="#!" data-mdb-ripple="true" data-mdb-ripple-color="light">
                     <img class="rounded-t-lg md:w-[350px] md:h-[200px]" src={event.media[0].url} alt=""/>
                   </a>
                   <div class="p-6">
                     <h5 class="text-gray-900 text-xl font-medium mb-2">{event.title}</h5>
                     <p class="text-gray-700 text-base mb-4">
                       {event.details.nl.shortdescription}
                     </p>
                     <span className="  inline-flex items-center rounded-full px-3 py-0.5 text-sm font-medium">
                          {event.location.city}
                      </span>
                   </div>
                 </div>
               </div>
              ))}
          </ul>
      </Layout>

  )
}


// const eventCards = ({events}) => (
//     return(
//     <>
//     {/* create a grid list with all the events using tailwind css */}
//     <Layout>
//     </>
//     )
//   )


// const Events() = events.map(events => {
//   return (
//     <div class="rounded overflow-hidden shadow-lg">
//       <img class="w-full" src={events.media[0].url} alt="Mountain"></img>
//       <div class="px-6 py-4">
//         <div class="font-bold text-xl mb-2">{events.title}</div>
//         <p class="text-gray-700 text-base">
//           {events.details.nl.shortdescription}
//         </p>
//       </div>
//       <div class="px-6 pt-4 pb-2">
//         <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#photography</span>
//         <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#travel</span>
//         <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
//       </div>
//     </div>
//   )
// }
// const Component = ({events}) => {
//   return(
//   <>
//   <Layout>
//     <div className="grid grid-cols-2 md:grid-flow-row">
//       <div>{events.map(renderEventCards)}</div>
//     </div>
//     </Layout>
//   </>
//   )
// }

  // ? Show how user if user is logged in and shows the email
  // const { data: session } = useSession()
  // if (session) {
  //   return <>
  //     Signed in as {session.user.email} <br />
  //     <img src={session.user.image} alt="" />
  //     <button onClick={() => signOut()}>Sign out</button>
  //   </>
  // }
  // return <>
  //   Not signed in <br />
  //   <button onClick={() => signIn()}>Sign in</button>
  // </>



export default Events;