import Image from "next/image";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About MGBW Group | Legacy of Trust Since 1940",
  description:
    "Pioneering excellence across diversified sectors with a tradition of trust since 1940.",
};

const leaders = [
  {
    name: "M. Govind Rao",
    role: "",
    description:
      "M. Govind Rao was a visionary industrialist and humanitarian whose life reflected humility, discipline, and compassion. A key pillar of Mangalore Ganesh Beedi, he played a significant role in expanding the business while upholding ethics, transparency, and respect for employees.",
    image: "/images/about/govind-rao.jpg",
  },
  {
    name: "DR. M Jagannath Shenoi",
    role: "Managing Partner, Mangalore Ganesh Beedi Works | Chairman, Silent Shores Resorts & Spa",
    description:
      "Dr. M. Jagannath Shenoi carries forward the tradition of the Shenoi family with a rare blend of business leadership and philanthropy. Taking charge of Mangalore Ganesh Beedi Works in the mid-1970s after the untimely loss of his father, he transformed challenges into opportunities.",
    image: "/images/about/jagannath-shenoi.jpg",
  },
  {
    name: "Govind J. Shenoy",
    role: "Executive Partner, MGBW Group",
    description:
      "Mr. Govind J. Shenoy represents the new generation of leadership at MGBW Group, combining a value-driven outlook with a modern, global perspective. He entered the family business at the age of 23 and has since been instrumental in strengthening its core operations while expanding into new sectors.",
    image: "/images/about/govind-shenoy.jpg",
  },
];

const values = [
  {
    title: "Integrity First",
    description: "Doing what's right across all operations",
  },
  {
    title: "People-Centric",
    description: "Empowering communities, respecting tradition",
  },
  {
    title: "Consistency in Quality",
    description: "Never compromising, always delivering",
  },
  {
    title: "Roots with Vision",
    description: "Honoring our past, building for the future",
  },
];

const verticals = [
  {
    name: "Mangalore Ganesh Beedi Works",
    desc: "Trusted name in beedi manufacturing and exports since 1940.",
    href: "/businesses/mangalore-ganesh-beedi",
  },
  {
    name: "Shukra Beedies LLP",
    desc: "High-volume production backed by consistency and quality since 1982.",
    href: "/businesses/shukra-beedi",
  },
  {
    name: "Silent Shores Resort & Spa",
    desc: "A luxury lakeside retreat in Mysuru offering refined hospitality.",
    href: "https://www.silentshores.com",
    external: true,
  },
  {
    name: "J&G Agarbatti",
    desc: "Premium incense sticks crafted with natural ingredients and a spiritual purpose.",
    href: "/businesses/jg-agarbatthi",
  },
  {
    name: "MGBW Garage",
    desc: "A digital space celebrating automotive culture, speed, and lifestyle.",
    href: "https://www.instagram.com/mgbwgarage",
    external: true,
  },
  {
    name: "501 Safety Matches",
    desc: "Complementary product introduced in 2025, crafted for everyday reliability.",
    href: "#",
  },
];

const stats = [
  { number: "1,00,000+", label: "Workforce" },
  { number: "6", label: "Business Verticals" },
  { number: "1000+", label: "Clients Worldwide" },
  { number: "5", label: "Facilities" },
];

export default function AboutPage() {
  return (
    <>
      {/* Hero */}
      <section className="relative h-[50vh] flex items-center justify-center bg-gray-900">
        <div className="absolute inset-0">
          <Image
            src="/images/about/about-hero.jpg"
            alt="About MGBW Group"
            fill
            className="object-cover opacity-40"
            priority
          />
        </div>
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-4xl md:text-6xl font-bold mb-4">
            About MGBW Group
          </h1>
          <p className="text-lg md:text-xl font-light">
            Pioneering excellence across diversified sectors with a tradition of
            trust since 1940.
          </p>
        </div>
      </section>

      {/* History */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold mb-2">Eight Decades.</h2>
          <p className="text-pink-600 text-xl mb-8">
            One Journey. Many Futures
          </p>
          <div className="text-gray-600 leading-relaxed space-y-4 text-lg">
            <p>
              MGBW Group is a family-led, values-driven enterprise built over
              eight decades of growth and trust. Established in 1940 with the
              founding of Mangalore Ganesh Beedi Works by{" "}
              <strong className="text-gray-900">
                Shri Bantwal Raghuram Prabhu &amp; Shri Madhav Shenoi
              </strong>
              , the Group has steadily evolved across sectors, ranging from
              tobacco and wellness to hospitality, fragrance, and automotive
              lifestyle.
            </p>
            <p>
              Guided by discipline, purpose, and people-first thinking, the MGBW
              Group&apos;s foundations are rooted in trust and ethical growth. What
              began as a humble venture has grown into a multi-vertical
              enterprise that continues to touch millions of lives, led today by{" "}
              <strong className="text-gray-900">
                Shri DR. M Jagannath Shenoi and Shri Govind J. Shenoy
              </strong>
              , who bring generational vision and stewardship to the business.
            </p>
            <p>
              At its core, MGBW stands not just for business excellence, but for
              building institutions that endure.
            </p>
          </div>
        </div>
      </section>

      {/* Vision & Mission */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto grid md:grid-cols-2 gap-12">
          <div>
            <h3 className="text-2xl font-bold mb-4">Our Vision</h3>
            <p className="text-gray-600 leading-relaxed">
              To be a progressive and diversified conglomerate that blends our
              heritage with innovation, creating lasting value across tobacco,
              FMCG, hospitality, and allied businesses — while steadfastly
              upholding The Tradition of Trust since 1940.
            </p>
          </div>
          <div>
            <h3 className="text-2xl font-bold mb-4">Mission</h3>
            <p className="text-gray-600 leading-relaxed">
              To uphold the Tradition of Trust by ensuring uncompromising quality
              and authenticity in every product and service.
            </p>
          </div>
        </div>
      </section>

      {/* Leadership */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4">
            Carrying Forward the Tradition with Vision
          </h2>
          <div className="grid md:grid-cols-3 gap-8 mt-12">
            {leaders.map((leader) => (
              <div
                key={leader.name}
                className="bg-gray-50 rounded-2xl overflow-hidden shadow-md"
              >
                <div className="relative h-64">
                  <Image
                    src={leader.image}
                    alt={leader.name}
                    fill
                    className="object-cover"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-bold">{leader.name}</h3>
                  {leader.role && (
                    <p className="text-pink-600 text-sm mt-1">{leader.role}</p>
                  )}
                  <p className="text-gray-600 text-sm mt-3 leading-relaxed">
                    {leader.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Values */}
      <section className="py-16 px-4 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Built on Values That Endure
          </h2>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {values.map((v) => (
              <div
                key={v.title}
                className="bg-white rounded-xl p-6 text-center shadow-sm"
              >
                <h3 className="font-bold text-lg mb-2">{v.title}</h3>
                <p className="text-gray-600 text-sm">{v.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Verticals */}
      <section className="py-20 px-4 bg-white">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">
            Our Verticals
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {verticals.map((v) => (
              <div
                key={v.name}
                className="border rounded-xl p-6 hover:shadow-md transition"
              >
                <h3 className="font-bold text-lg mb-2">{v.name}</h3>
                <p className="text-gray-600 text-sm mb-4">{v.desc}</p>
                {v.external ? (
                  <a
                    href={v.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-pink-600 text-sm font-semibold hover:underline"
                  >
                    Learn more →
                  </a>
                ) : v.href !== "#" ? (
                  <Link
                    href={v.href}
                    className="text-pink-600 text-sm font-semibold hover:underline"
                  >
                    Learn more →
                  </Link>
                ) : null}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-16 px-4 bg-pink-600 text-white">
        <div className="max-w-4xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          {stats.map((s) => (
            <div key={s.label}>
              <div className="text-4xl font-bold">{s.number}</div>
              <div className="text-sm mt-2 opacity-90">{s.label}</div>
            </div>
          ))}
        </div>
        <p className="text-center mt-8 max-w-2xl mx-auto opacity-90">
          Together, they represent a perfect harmony of experience and evolution,
          committed to growing the MGBW Group with purpose, responsibility, and
          resilience.
        </p>
      </section>
    </>
  );
}
