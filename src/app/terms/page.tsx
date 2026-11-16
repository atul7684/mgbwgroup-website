import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Terms & Conditions | MGBW Group",
  description: "Terms and Conditions for MGBW Group website.",
};

export default function TermsPage() {
  return (
    <section className="py-20 px-4 bg-white">
      <div className="max-w-3xl mx-auto prose prose-gray">
        <h1>Terms &amp; Conditions</h1>
        <p>
          Welcome to the official website of <strong>MGBW Group</strong>. By
          accessing or using our website, you agree to comply with and be bound
          by the following Terms &amp; Conditions.
        </p>

        <h2>1. Use of the Website</h2>
        <p>
          The content on this website is provided for general informational
          purposes only. You may not use the website for unlawful purposes, to
          distribute harmful material, or to disrupt its operation.
        </p>

        <h2>2. Intellectual Property Rights</h2>
        <p>
          All text, images, graphics, logos, designs, and other content on this
          website are the property of MGBW Group unless otherwise stated. You may
          not reproduce, distribute, or use any content without prior written
          consent.
        </p>

        <h2>3. Business Inquiries &amp; Partnerships</h2>
        <p>
          Any inquiry or application submitted through this website does not
          constitute a binding agreement. MGBW Group reserves the right to
          evaluate and accept or reject inquiries at its sole discretion.
        </p>

        <h2>4. Third-Party Links</h2>
        <p>
          Our website may contain links to third-party websites. These links are
          provided for convenience only. MGBW Group is not responsible for the
          content, accuracy, or policies of external sites.
        </p>

        <h2>5. Disclaimer of Liability</h2>
        <p>
          While we strive to keep the information accurate and up to date, MGBW
          Group makes no warranties regarding completeness, reliability, or
          accuracy. We are not liable for any loss or damage arising from the use
          of this website.
        </p>

        <h2>6. Privacy</h2>
        <p>
          Use of this website is also governed by our{" "}
          <a href="/privacy">Privacy Policy</a>.
        </p>

        <h2>7. Changes to Terms</h2>
        <p>
          MGBW Group reserves the right to update or modify these Terms at any
          time. Updates will be posted on this page.
        </p>

        <h2>8. Governing Law</h2>
        <p>
          These Terms shall be governed by the laws of India. Any disputes shall
          be subject to the exclusive jurisdiction of the courts in Mysuru,
          Karnataka.
        </p>

        <h2>9. Contact Us</h2>
        <p>
          MGBW Group<br />
          Email: <a href="mailto:mgbwworks@gmail.com">mgbwworks@gmail.com</a><br />
          Phone: 0821-2420241<br />
          Address: Head Office, Vinoba Road, Mysore-570005
        </p>
      </div>
    </section>
  );
}
