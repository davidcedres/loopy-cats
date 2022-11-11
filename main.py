import streamlit as st
import defs as defs
# import time

st.title('Loopy Cats')

st.header('Cat models')
st.caption('The purple ')
st.image('./assets/automaton.png')

st.header('Controllers')
st.image('./assets/controllers.png')


st.header('Simulation')
cat_type = st.selectbox('Cat', ('Normal', 'Crazy'))
controller_type = st.selectbox('Controller', ('Open Loop', 'Closed Loop'))

cat = defs.Cat(type=cat_type)
controller = defs.OpenLoopController(
) if controller_type == 'Open Loop' else defs.ClosedLoopController()

t = 0
t_max = 20

events = ['TIME']

while len(events) != 0:
    event = events.pop(0)

    # print current state
    st.subheader('Time = {}, Event = {}'.format(t, event))

    col1, col2 = st.columns(2)

    with col1:
        st.caption(cat.state)
        st.image('./assets/{}.gif'.format(cat.sprite()))

    # actuate on the cat
    output = cat.input(event)

    with col2:
        if output:
            st.caption(output)
            st.image('./assets/{}.gif'.format(output.lower()))

    command = controller.input(
        '1' if controller_type == 'Open Loop' else output)

    events.append(command)

    # next iter
    # time.sleep(.5)
    t = t + 1

    if t == t_max + 1:
        st.caption('DONE')
        break
