import re

def select(el, all=False):
    el = el.strip()
    if all:
        return list(document.querySelectorAll(el))
    else:
        return document.querySelector(el)

def on(type, el, listener, all=False):
    select_el = select(el, all)
    if select_el:
        if all:
            for e in select_el:
                e.addEventListener(type, listener)
        else:
            select_el.addEventListener(type, listener)

def onscroll(el, listener):
    el.addEventListener('scroll', listener)

navbarlinks = select('#navbar .scrollto', True)

def navbarlinks_active():
    position = window.scrollY + 200
    for navbarlink in navbarlinks:
        if not navbarlink.hash:
            continue
        section = select(navbarlink.hash)
        if not section:
            continue
        if position >= section.offsetTop and position <= (section.offsetTop + section.offsetHeight):
            navbarlink.classList.add('active')
        else:
            navbarlink.classList.remove('active')

window.addEventListener('load', navbarlinks_active)
onscroll(document, navbarlinks_active)

def scrollto(el):
    header = select('#header')
    offset = header.offsetHeight

    element_pos = select(el).offsetTop
    window.scrollTo({
        'top': element_pos - offset,
        'behavior': 'smooth'
    })

select_header = select('#header')
select_topbar = select('#topbar')
if select_header:
    def header_scrolled():
        if window.scrollY > 100:
            select_header.classList.add('header-scrolled')
            if select_topbar:
                select_topbar.classList.add('topbar-scrolled')
        else:
            select_header.classList.remove('header-scrolled')
            if select_topbar:
                select_topbar.classList.remove('topbar-scrolled')
    window.addEventListener('load', header_scrolled)
    onscroll(document, header_scrolled)

backtotop = select('.back-to-top')
if backtotop:
    def toggle_backtotop():
        if window.scrollY > 100:
            backtotop.classList.add('active')
        else:
            backtotop.classList.remove('active')
    window.addEventListener('load', toggle_backtotop)
    onscroll(document, toggle_backtotop)

on('click', '.mobile-nav-toggle', lambda e: (
    select('#navbar').classList.toggle('navbar-mobile'),
    this.classList.toggle('bi-list'),
    this.classList.toggle('bi-x'),
))

on('click', '#navbar .dropdown-menu', lambda e: e.stopPropagation())
on('click', '#navbar .
